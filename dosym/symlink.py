# Symlink Class File
# Each symlink from input file creates an instance of the Symlink Class
from dosym import logging

logger = logging.create_symlink_logger()

class DoSymlinks:
    def __init__(self):
        logger.debug("Instantiated symlink class")
        self.symlinks = {}
        self.validated_symlinks = {}
        self.invalidated_symlinks = {}

    def add_symlink(self, symlink_key, symlink_val):
        self.symlinks[symlink_key] = symlink_val
        self._validate_symlinks();

    def _validate_symlinks(self):
        pass
            

    def create_symlinks(self):
        pass
