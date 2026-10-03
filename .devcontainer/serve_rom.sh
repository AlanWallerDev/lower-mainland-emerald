#!/bin/sh
# Serve the built ROM on port 8000 so it can be downloaded from a phone browser
# (the editor's file-list menu is hard to use on mobile). Private to your codespace.
mkdir -p /tmp/rom
[ -f pokeemerald_modern.gba ] && cp pokeemerald_modern.gba /tmp/rom/
nohup python3 -m http.server 8000 --directory /tmp/rom > /tmp/rom-server.log 2>&1 &
