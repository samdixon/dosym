# Symlink Class File
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

def add_symlinks_helper(processed_input_data): 
    """
    Simple helper function that adds symlinks to Symlinks class
    """
    symlinks_buffer = list()
    for key, val in processed_input_data.localpath_symlinks.items():
        symlinks_buffer.append(Symlink(key,val))
        logger.debug(f"Adds {key}: {val} to Symlinks List")

    logger.debug(f"Symlinks: {symlinks_buffer}")
    return symlinks_buffer


class Symlink(object):
    """Class to create a single instance of a Symlink"""

    CREATED = "created"
    FAILED = "failed"
    BROKEN = "broken"

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.absolute_src = self._get_absolute_path(self.src)
        self.absolute_dest = self._get_absolute_path(self.dest)
        self.is_valid_src = self._validate_src()
        self.is_valid_dest_path = self._validate_dest_path()
        self.file_type = None
        if self.is_valid_src:
            self.file_type = self._check_file_type() 
        self.dest_already_symlink = False
        self.status = None
        self.error_message = None

    def _get_absolute_path(self, item):
        return os.path.expanduser(item)

    def _validate_src(self):
        return os.path.exists(self.absolute_src)

    def _pop_dest_file(self):
        s = self.absolute_dest.split("/")
        s.pop()
        return "/".join(s) 

    def _validate_dest_path(self):
        if os.path.exists(self._pop_dest_file()): 
            return True
        else:
            try:
                os.makedirs(self._pop_dest_file())
                self._validate_dest_path()
                return True
            except:
                logger.error(f"Attempted to create {self._pop_dest_file()} and failed.")
                return False

    def _check_file_type(self):
        if os.path.isdir(self.absolute_src):
            return 'directory'
        elif os.path.isfile(self.absolute_src):
            return 'file'
        else:
            logger.error("Error in _check_file_type function")

    def _make_paths(self):
        pass

    def _simple_create(self):
        try:
            os.symlink(self.absolute_src, self.absolute_dest)
            self.status = self.CREATED
        except FileExistsError as e:
            self.status = self.FAILED
            self.error_message = e
            logger.debug(f"{e}")

    def _force_create(self):
        try:
            subprocess.call(
                    f"ln -sfn {self.absolute_src} {self.absolute_dest}", 
                    shell=True)
            if self.is_valid_src:
                self.status = self.CREATED
            elif not self.is_valid_src:
                self.status = self.BROKEN
            else:
                pass
        except Exception as e:
            self.status = self.FAILED
            logger.error(f"{e}")
            pass

    def create(self, force):
        if force:
            logger.debug(
                    f"Attempting to force create link {self.src} {self.dest}")
            self._force_create()
        else:
            logger.debug(f"Attempting to create link {self.src} {self.dest}")
            self._simple_create()


