from __future__ import unicode_literals
from playlist_watcher.runner import Runner
import sys
import argparse
import json

ydl_opts = {"quiet": True, "outtmpl": "./youtube/%(title)s.%(ext)s"}

if __name__ == "__main__":
    print(sys.argv[1:])
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--logbook_name', action="store")
    parser.add_argument('-p', '--playlists_name', action="store")
    args = parser.parse_args(sys.argv[1:])

    runner = Runner(ydl_opts, args.playlists_name, args.logbook_name, 60)
    runner.run()



