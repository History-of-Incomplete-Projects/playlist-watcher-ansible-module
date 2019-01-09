from __future__ import unicode_literals
from playlist_watcher.runner import Runner
import sys
import argparse
import json
import os

ydl_opts = {"quiet": True, "outtmpl": "./youtube/%(title)s.%(ext)s"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--logbook_name', action="store")
    parser.add_argument('-p', '--playlists_name', action="store")
    args = parser.parse_args(sys.argv[1:])

    runner = Runner(ydl_opts, args.playlists_name, args.logbook_name, 60)
    
    # https://stackoverflow.com/questions/788411/check-to-see-if-python-script-is-running
    pid = str(os.getpid())
    pidfile = "/tmp/playlist-watcher-ansible-module.pid"

    if os.path.isfile(pidfile):
        print "%s already exists, exiting" % pidfile
        sys.exit()
    file(pidfile, 'w').write(pid)
    try:
        runner.run()
    finally:
        os.unlink(pidfile)



