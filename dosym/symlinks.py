# Symlink Class File
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

"""
Simple helper function that adds symlinks to Symlinks class
"""
def add_symlinks_helper(symlink_object, processed_input_data) -> None:
    for key, val in processed_input_data.localpath_symlinks.items():
        symlink_object.add_symlink(key, val)

"""
Class that validates and creates Symlinks
This class may have slightly too much responsibility
It may make more sense to split it up into a SymlinkValidation &
SymlinkMaker class. 
In very early stages. Currently only shelling out to a singular
command with no optional flags
"""
class Symlinks:
    def __init__(self):
        self.symlinks = {}
        self.validated_symlinks = {}
        self.invalidated_symlinks = {}

    def add_symlink(self, symlink_key, symlink_val):
        if self._validate_symlink_key(symlink_key):
            self.validated_symlinks[symlink_key] = symlink_val
        else:
            self.invalidated_symlinks[symlink_key] = symlink_val

    def _validate_symlink_key(self, symlink_key) -> bool:
        return os.path.exists(os.path.expanduser(symlink_key))

    def _validate_symlink_val(self, symlink_val) -> bool:
        pass

    def create_symlinks(self):
        for key, val in self.validated_symlinks.items():
            subprocess.call("ln -sfn {} {}".format(key,val), shell=True)
