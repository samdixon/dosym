# Symlink Class File
# Each symlink from input file creates an instance of the Symlink Class
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

# Class that transforms form input data into usable data
# For other classes such as Symlinks
class Symlinks:
    def __init__(self):
        logger.debug("Instantiated symlink class")
        self.symlinks = {}
        self.validated_symlinks = {}
        self.invalidated_symlinks = {}

    def add_symlink(self, symlink_key, symlink_val):
        if self._validate_symlink(symlink_key):
            self.validated_symlinks[symlink_key] = symlink_val
        else:
            self.invalidated_symlinks[symlink_key] = symlink_val

    def _validate_symlink(self, symlink_key) -> bool:
        return os.path.exists(os.path.expanduser(symlink_key))
            

    def create_symlinks(self):
        for key, val in self.validated_symlinks.items():
            subprocess.call("ln -sfn {} {}".format(key,val), shell=True)
