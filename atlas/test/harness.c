// Headless test harness: runs the ROM with scripted input and writes screenshots.
// Build: cc -O2 -o build/harness atlas/test/harness.c -lmgba
// Usage: build/harness rom.gba script.txt [save.sav]
// Script lines:  wait N | press KEYS [N] | hold KEYS N | repeat KEYS N | shot file.ppm
//                savestate file | loadstate file | peek HEXADDR [N] | setflag SB1PTR FLAG | # comment
// KEYS: A B SELECT START RIGHT LEFT UP DOWN R L joined with '+', e.g. press A, hold UP+B 30.
#include <mgba/core/core.h>
#include <mgba/core/config.h>
#include <mgba/core/log.h>
#include <mgba-util/vfs.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static struct mCore *core;
static color_t *buffer;
static unsigned width, height;

static int parseKeys(char *s) {
	static const char *names[] = {"A", "B", "SELECT", "START", "RIGHT", "LEFT", "UP", "DOWN", "R", "L"};
	int keys = 0;
	for (char *tok = strtok(s, "+"); tok; tok = strtok(NULL, "+")) {
		for (int i = 0; i < 10; i++)
			if (!strcmp(tok, names[i])) keys |= 1 << i;
	}
	return keys;
}

static void run(int frames, int keys) {
	core->setKeys(core, keys);
	for (int i = 0; i < frames; i++) core->runFrame(core);
	core->setKeys(core, 0);
}

static void shot(const char *path) {
	FILE *f = fopen(path, "wb");
	if (!f) { perror(path); return; }
	fprintf(f, "P6\n%u %u\n255\n", width, height);
	for (unsigned i = 0; i < width * height; i++) {
		color_t c = buffer[i];
		unsigned char rgb[3] = {c & 0xFF, (c >> 8) & 0xFF, (c >> 16) & 0xFF};
		fwrite(rgb, 1, 3, f);
	}
	fclose(f);
}

static void quiet(struct mLogger *l, int category, enum mLogLevel level, const char *fmt, va_list args) {
	(void) l; (void) category; (void) level; (void) fmt; (void) args;
}

int main(int argc, char **argv) {
	static struct mLogger logger = { .log = quiet };
	mLogSetDefaultLogger(&logger);
	if (argc < 3) { fprintf(stderr, "usage: %s rom script [save]\n", argv[0]); return 2; }
	core = mCoreFind(argv[1]);
	if (!core || !core->init(core)) { fprintf(stderr, "no core\n"); return 1; }
	mCoreInitConfig(core, NULL);
	core->desiredVideoDimensions(core, &width, &height);
	buffer = calloc(width * height, sizeof(color_t));
	core->setVideoBuffer(core, buffer, width);
	if (!mCoreLoadFile(core, argv[1])) { fprintf(stderr, "load failed\n"); return 1; }
	if (argc > 3) {
		struct VFile *sv = VFileOpen(argv[3], O_CREAT | O_RDWR);
		if (sv) core->loadSave(core, sv);
	}
	core->reset(core);

	FILE *sc = fopen(argv[2], "r");
	if (!sc) { perror(argv[2]); return 1; }
	char line[256];
	while (fgets(line, sizeof line, sc)) {
		char cmd[32] = "", arg[128] = "";
		int n = 0;
		int got = sscanf(line, "%31s %127s %d", cmd, arg, &n);
		if (got < 1 || cmd[0] == '#') continue;
		if (!strcmp(cmd, "wait")) run(atoi(arg), 0);
		else if (!strcmp(cmd, "press")) { run(got >= 3 ? n : 6, parseKeys(arg)); run(10, 0); }
		else if (!strcmp(cmd, "hold")) run(n, parseKeys(arg));
		else if (!strcmp(cmd, "shot")) shot(arg);
		else if (!strcmp(cmd, "savestate")) {
			size_t size = core->stateSize(core);
			void *buf = malloc(size);
			if (core->saveState(core, buf)) {
				FILE *f = fopen(arg, "wb");
				if (f) { fwrite(buf, 1, size, f); fclose(f); }
			}
			free(buf);
		}
		else if (!strcmp(cmd, "loadstate")) {
			size_t size = core->stateSize(core);
			void *buf = malloc(size);
			FILE *f = fopen(arg, "rb");
			if (f && fread(buf, 1, size, f) == size) core->loadState(core, buf);
			else fprintf(stderr, "loadstate failed: %s\n", arg);
			if (f) fclose(f);
			free(buf);
		}
		else if (!strcmp(cmd, "peek")) {
			// peek ADDR N: print N 32-bit words starting at hex ADDR
			unsigned addr = strtoul(arg, NULL, 16);
			printf("%08x:", addr);
			for (int i = 0; i < (got >= 3 ? n : 1); i++) printf(" %08x", core->busRead32(core, addr + i * 4));
			printf("\n");
		}
		else if (!strcmp(cmd, "setflag")) {
			// setflag SB1PTR FLAG: set a save flag. SB1PTR is the address of gSaveBlock1Ptr (run.sh
			// fills in @gSaveBlock1Ptr from the map file); flags live at offset 0x1270 of SaveBlock1.
			unsigned ptrAddr = strtoul(arg, NULL, 16);
			unsigned base = core->busRead32(core, ptrAddr) + 0x1270;
			core->busWrite8(core, base + n / 8, core->busRead8(core, base + n / 8) | (1 << (n % 8)));
		}
		else if (!strcmp(cmd, "repeat")) {
			// repeat KEYS N: press KEYS N times (useful for mashing through text)
			char keys[128]; strcpy(keys, arg);
			for (int i = 0; i < n; i++) { char k[128]; strcpy(k, keys); run(6, parseKeys(k)); run(14, 0); }
		}
	}
	core->deinit(core);
	return 0;
}
