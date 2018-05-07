#!/usr/bin/env python

import os, sys, time

class FileWatcher:
    def __init__(self):
        print("Initializing watcher...")
        self.new_files = []
        self.cleaned_new_files_container = True


    def files_to_timestamp(self, path):
        files = [os.path.join(path, f) for f in os.listdir(path)]
        return dict ([(f, os.path.getmtime(f)) for f in files])

    def watch(self, path_to_watch, interval=5):
        # path_to_watch = sys.argv[1]
        print("Watching {}".format(path_to_watch))

        before = self.files_to_timestamp(path_to_watch)

        while True:
            time.sleep (interval)
            after = self.files_to_timestamp(path_to_watch)

            added = [f for f in after.keys() if not f in before.keys()]
            removed = [f for f in before.keys() if not f in after.keys()]
            modified = []

            for f in before.keys():
                if not f in removed:
                    if os.path.getmtime(f) != before.get(f):
                        modified.append(f)

            if added: print "Added: ", ", ".join(added)
            if removed: print "Removed: ", ", ".join(removed)
            if modified: print "Modified ", ", ".join(modified)

            if len(added) > 0:
                if not self.cleaned_new_files_container:
                    new_files.append(added)
                else:
                    new_files = added

            before = after

    def get_new_files(self):
        return self.new_files

    def clear_new_files_container(self):
        self.new_files = []
        self.cleaned_new_files_container = true
