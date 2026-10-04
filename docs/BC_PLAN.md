# BC Emerald: expansion plan

Approved 2026-10-04 (logged in Living Atlas `docs/DECISIONS.md`). Decided: option C map
approach, 202-entry all-BC Field Journal, starters, CINDER and RIPTIDE, legendaries, public
repo, drop the "Lower Mainland Emerald" title. Still open: new title, Indigenous content.
All story names and lines below are stand-ins.

## Where the hack is today

- Engine work is done: 15 Living Atlas types, Nuzlocke mode, game speed, terminology pass,
  stand-in sprites for all 386 slots, habitat-based wild encounters, historical BC names for
  key characters, themed gyms.
- The world is still Hoenn with new names. Map shapes, story, villains, legendaries and
  lore are Emerald's.
- Only **73 of 386** organisms are truly local (local score 100 in `atlas/species_map.json`).
  The rest are worldwide fill (Arabica Coffee, Tobacco Mosaic Virus, Mother of Thousands sit in
  the starter slots). The Living Atlas database has too few BC species to fill a BC game.

## Goal

A game that feels like BC from end to end: BC places in a believable layout, BC organisms
in their real habitats, a story built on BC's real natural forces, and lore drawn from BC
natural history and science.

## 1. World

### Scope options

| Option | What | Cost | Result |
|---|---|---|---|
| A. Re-theme | Keep Hoenn maps, rename, new story | Low | Geography stays scrambled |
| B. New region | Draw a new BC region map by map | Very high (months) | Most authentic |
| **C. Hybrid (recommended)** | Keep Hoenn's map graph, reassign each part to a BC region by biome, new BC tiles, BC TrailNav map, a few new signature maps. Rebuild single routes later if wanted. | Medium | Stylized but coherent BC |

### Region layout under option C

Hoenn's west becomes the Lower Mainland, the southern sea becomes the Salish Sea and
Vancouver Island, the north becomes the Interior, and the eastern sea becomes the North Coast.

| Hoenn | Now | Proposed | Region | Why |
|---|---|---|---|---|
| Littleroot | LADNER | LADNER | Lower Mainland | Delta farm town start |
| Oldale | TSAWWASSEN | TSAWWASSEN | Lower Mainland | |
| Petalburg | RICHMOND | RICHMOND | Lower Mainland | Parent's gym |
| Petalburg Woods | PACIFIC SPIRIT | PACIFIC SPIRIT | Lower Mainland | |
| Rustboro | BURNABY | **SQUAMISH** | Sea to Sky | STONE gym (MUNDAY), granite, mining company HQ |
| Rusturf Tunnel | CASSIAR TUNNEL | **OTHELLO TUNNELS** | Fraser Canyon | Real rail tunnels |
| Dewford | BOWEN ISLAND | **TOFINO** | Vancouver Island | BRAWN gym (JEROME), surf |
| Granite Cave | GARDNER CAVE | **HORNE LAKE CAVES** | Vancouver Island | Real cave park |
| Slateport | STEVESTON | **VICTORIA** | Vancouver Island | Museum = Royal BC Museum, harbour |
| Route 110 | HWY 99 | **GALLOPING GOOSE** | Vancouver Island | Real bike trail = Cycling Road |
| Mauville | SURREY | **HOPE** | Fraser Valley | CHARM gym (FRASER); BC's highway crossroads |
| Verdanturf | LANGLEY | **YALE** | Fraser Canyon | Gold rush town |
| Route 111 desert | FRASER FLATS | **THOMPSON GRASSLANDS** | Interior | Dust storms, hoodoos |
| Mt. Chimney | MT. GARIBALDI | **WELLS GRAY CONE** | Interior | Real volcanic field |
| Fallarbor | ABBOTSFORD | **KAMLOOPS** | Interior | Ash fall becomes wildfire smoke |
| Lavaridge | HARRISON | HARRISON | Fraser Valley | EMBER gym (CARR), hot springs |
| Fortree | MAPLE RIDGE | **REVELSTOKE** | Columbia Mountains | SKY gym (MACGILL), inland rainforest |
| Lilycove | VANCOUVER | VANCOUVER | Lower Mainland | Big city, department store |
| Mossdeep | GIBSONS | **PRINCE RUPERT** | North Coast | MIND gym; ocean observatory replaces the space center |
| Seafloor Cavern | GEORGIA DEEP | **HECATE SPONGE REEF** | North Coast | 9,000-year-old glass sponge reefs |
| Sootopolis | DEEP COVE | DEEP COVE | Lower Mainland | AQUA gym (FORTES) |
| Pacifidlog | POINT ROBERTS | **ECHO BAY** | Broughton Archipelago | Float-home village |
| Abandoned Ship | (unchanged) | **SS BEAVER WRECK** | Burrard Inlet | Real 1888 wreck |
| Sky Pillar | STAWAMUS CHIEF | STAWAMUS CHIEF | Sea to Sky | Peregrines nest on it |
| Victory Road / Ever Grande | SEA TO SKY / WHISTLER | same | Sea to Sky | Nature League |

Sea routes 124 to 134 become Inside Passage waters (Hecate Strait, Johnstone Strait,
Queen Charlotte Sound...).

### World work

- New tiles: conifers (Douglas-fir, cedar), snow and alpine, arbutus coast, sagebrush
  grassland, cannery and float-home buildings. Start with palette swaps of Emerald tiles.
- Redraw the TrailNav (region map) as a stylized BC.
- Signature new maps (later phase): Burgess Shale dig in Yoho, Adams River salmon run,
  Hecate sponge reef dive.

## 2. Creatures

### Roster

- **BC Field Journal of 202** (Emerald's regional count), every entry native to BC
  (a handful of well-known invasives flagged as such, see story).
- The other 184 national slots stay worldwide Living Atlas organisms, met after the
  credits (trades, Burns Bog safari, Frontier).
- About 130 new BC species are needed. Proposal: keep them in this repo as
  `atlas/bc_species.json` with the Living Atlas schema and `bc-001` ids, so the Living
  Atlas database stays untouched. Stats are authored to fit their Emerald slot.

### Candidates by habitat (sample)

| Habitat | Candidates |
|---|---|
| Rivers | Sockeye, coho, chinook, chum and pink salmon, white sturgeon, eulachon, steelhead, American dipper |
| Coast and sea | Sea otter, Steller sea lion, harbour seal, Dall's porpoise, Dungeness crab, sunflower sea star, ochre star, geoduck, opalescent nudibranch, wolf eel, lingcod, bull kelp, eelgrass |
| Old growth | Douglas-fir, western redcedar, Sitka spruce, marbled murrelet, spotted owl, northern flying squirrel, Douglas squirrel, chanterelle, devil's club, skunk cabbage |
| Mountains | Hoary marmot, Vancouver Island marmot, pika, mountain caribou, cougar, lynx, white-tailed ptarmigan |
| Interior grassland | Western rattlesnake, burrowing owl, badger, sagebrush, bighorn sheep (have), mule deer |
| Wetlands and delta | Snow goose, sandhill crane, trumpeter swan, great blue heron, Pacific tree frog, rough-skinned newt, painted turtle |
| Everywhere | Steller's jay (provincial bird), black bear, coyote, northwestern crow, Anna's hummingbird, rufous hummingbird |
| Fire | Fire-chaser beetle, lodgepole pine (cones open in fire), fireweed, morel |
| Invasive | European green crab, American bullfrog, Himalayan blackberry, Japanese knotweed, eastern grey squirrel |
| Fossils | Burgess Shale (Anomalocaris, Opabinia, Hallucigenia, Pikaia: already in the database), Courtenay elasmosaur, Tumbler Ridge dinosaurs |

### Evolution (real life stages only)

Sockeye alevin to smolt to spawner, Pacific tree frog tadpole to frog, rough-skinned newt
eft to newt, Dungeness crab megalopa to crab, darner nymph to dragonfly, moon jelly polyp
to medusa (have), tiger swallowtail caterpillar to butterfly (have).

### Starters (decided)

| Slot | Organism | Type | Stages | Note |
|---|---|---|---|---|
| Treecko | Skunk Cabbage | Verdant | seed, seedling, flowering plant | Warms itself to melt through snow |
| Torchic | Morel | Ember | spore, mycelium, fruiting body | Fruits in burned forest the spring after a fire |
| Mudkip | American Beaver (`na-136`) | Aqua | kit, yearling, adult | Already in this slot |

### Legendaries and mythicals

Owner rule: legendaries are **very rare** organisms; mythicals are BC cryptids. Picks within
that rule were delegated to Claude.

| Slot | Organism | Why |
|---|---|---|
| Groudon (land) | Spirit bear (Kermode) | A few hundred white black bears, almost all on the North Coast; CINDER's target |
| Kyogre (sea) | Hecate glass sponge reef | Thought extinct for 40 million years until found in 1987; RIPTIDE's target |
| Rayquaza (sky) | Marbled Murrelet | Seabird that nests high in old growth; its nest stayed unknown until 1974. Links land and sea, so it calms both |
| Latias/Latios (roaming) | Vancouver Island Marmot pair | One of the rarest mammals on Earth (under 30 in the wild in 2003) |
| Regis | Opabinia (`fo-005`), Pikaia (`fo-009`), Marrella (new) | Burgess Shale, found only in BC; sealed in the Yoho dig |
| Root/Claw fossils | Hallucigenia (`fo-006`), Anomalocaris (`fo-004`) | Burgess Shale |
| Mew (Faraway Island) | **Sasquatch** | Hide-and-seek in deep forest grass |
| Lugia (Navel Rock) | **Caddy** (Cadborosaurus) | Sea serpent named by a Victoria paper in 1933 |
| Deoxys (Birth Island) | **Ogopogo** | Island becomes Rattlesnake Island, Okanagan Lake |

Cryptids use their common English names only. Their Field Journal entries describe
reported sightings, not invented biology, and draw on no Indigenous stories or art. Their
islands should be reachable after the credits without event tickets.

## 3. Story (stand-in outline, owner's call)

**Theme: a province of fire and flood.** Emerald's land vs sea becomes BC's two real
extremes: wildfire summers and atmospheric rivers.

- **CINDER** (Team Magma slot): believes the old forests must burn to be renewed. Wants to
  wake the land legendary and bring endless dry heat. Uses fire-linked and invasive organisms.
- **RIPTIDE** (Team Aqua slot): believes the sea should take back the delta. Wants the sea
  legendary and endless rain.
- Both are fictional and not modelled on any real group, company or movement. Real
  disasters (Lytton, the 2021 floods) are not blamed on them or named.

Beats, following Emerald's order:

1. Move to LADNER. PROF. MACOUN is chased on River Road; choose a starter.
2. RICHMOND: parent's gym, meet WALLY.
3. PACIFIC SPIRIT: CINDER grunt robs a mining company researcher.
4. SQUAMISH: MUNDAY's gym. Chase through the OTHELLO TUNNELS.
5. Boat to TOFINO: JEROME's gym; deliver a letter to DAWSON (Steven Stone slot, named
   for geologist George Mercer Dawson) in HORNE LAKE CAVES.
6. VICTORIA: both teams clash at the Royal BC Museum over submarine parts.
7. HOPE: FRASER's gym. Interior opens.
8. THOMPSON GRASSLANDS, KAMLOOPS under smoke, WELLS GRAY CONE: CINDER tries to force an
   eruption with the meteorite.
9. HARRISON: CARR's gym, then the parent's gym.
10. REVELSTOKE: MACGILL's gym.
11. VANCOUVER: RIPTIDE's hideout; they steal the submarine.
12. PRINCE RUPERT: the MIND twins' gym and the observatory.
13. HECATE SPONGE REEF: the sea legendary wakes. Heat dome and atmospheric river collide
    over DEEP COVE. Climb the STAWAMUS CHIEF for the sky legendary.
14. DEEP COVE: FORTES's gym.
15. SEA TO SKY, then the Nature League at WHISTLER.
16. After the credits: Burgess Shale dig (Regis), roaming spirit bears, the Frontier.

## 4. Lore

- **Natural history first.** Salmon feed the forest (salmon nitrogen shows up in tree
  rings), old growth, 9,000-year-old sponge reefs, the Burgess Shale. Every Field Journal
  entry is a real fact.
- **Science and exploration.** Field notebooks of MACOUN (botanist) and DAWSON (Geological
  Survey) replace the Regi braille puzzles as the trail to the sealed chambers.
- **Settler-era history as background:** Steveston canneries, the Fraser gold rush at
  Yale, the railway, logging and hydro dams. Told through signs, books and NPCs.
- **Indigenous content: needs an owner decision.** Recommendation: use place names as they
  are commonly used, and do not use sacred figures (Thunderbird, Sasq'ets, Sisiutl), crests,
  formline art or stories without consent from the Nations involved.

## 5. Phases

| Phase | Work | Rough size |
|---|---|---|
| 0. Housekeeping | `docs/STATE.md` and `docs/TASKS.md` here, verify the build | 1 session |
| 1. Design lock | Owner answers the open questions; final place table; final 202 roster list | 1 to 2 sessions |
| 2. Roster | `bc_species.json`, picker change (BC-only regional journal), sprites through the existing rigs, learnsets, wild tables by real habitat | 4 to 6 sessions |
| 3. World | Renames, BC TrailNav map, tile palette swaps, signs | 3 to 4 sessions |
| 4. Story | New teams, legendaries, all dialogue area by area, with mGBA scripted checks | 6 to 10 sessions |
| 5. Signature maps | Burgess dig, salmon run, sponge reef | 3 to 6 sessions |
| 6. Polish | Overworld creature sprites, back sprites, move names, playtest fixes | ongoing |

Each phase ends with a playable build and headless mGBA screenshots.

## Open questions

1. New title (and whether to rename the GitHub repo).
2. Indigenous content beyond the cryptids: the recommendation above?
