#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Minecraft Enhancement Hacker
URL: https://github.com/spezifanta/Minecraft-Enhancement-Hacker
"""

from __future__ import print_function

import argparse
import os
import sys

try:
    import nbt
except ImportError, error:
   nbt = None

__author__ = 'spezi|Fanta'
__version__ = '0.0.2'
__license__ = 'MIT'

def do_hack(player_file, level):
    """Load, hack, save player_file"""
    try:
        data = nbt.loadFile(player_file)
    except:
        sys.exit("'%s' could not be loaded." % (player_file))

    # Check for single or multiplayer player.dat
    if 'Data' in data: # Singleplayer
        player_data = data['Data']['Player']
    else:
        player_data = data

    try:
        player_data['XpLevel'].value = level
    except KeyError:
        sys.exit("Could not find key 'XpLevel'.")

    try:
        data.save(player_file)
    except:
        sys.exit('Something went horribly wrong.')
    else:
        print("Successfully updated '%s' to level %s."
              % (os.path.basename(player_file), level))

def run():
    """Parse arguments first"""
    parser = argparse.ArgumentParser(description='Enhancement Hacker.')
    parser.add_argument('player_file', metavar='PLAYER.DAT',
                        help='Path to Player.dat you wish to hack')
    parser.add_argument('level', metavar='XP_LEVEL', type=int,
                        help='Give a XP Level which you wish to reach')
    args = parser.parse_args()
    do_hack(args.player_file, args.level)

if __name__ == '__main__':
    if nbt:
        run()
    else:
        print("%s. NBT libary required!\nRun:\n\n\t"\
              " wget https://raw.github.com/codewarrior0/pymclevel/master/nbt.py"
              % error)
