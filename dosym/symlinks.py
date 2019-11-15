# Symlink Class File
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

"""
Simple helper function that adds symlinks to Symlinks class
"""
def add_symlinks_helper(processed_input_data): 
    buf = list()
    for key, val in processed_input_data.localpath_symlinks.items():
        buf.append(Symlink(key,val))
        logger.debug(f"Adds {key}: {val} to Symlinks List")

    return buf


class Symlink():
    """Class to create a single instance of a Symlink"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.absolute_src = self._get_absolute_path(self.src)
        self.absolute_dest = self._get_absolute_path(self.dest)
        self.valid_src = self._validate_src()
        self.valid_dest_path = self._validate_dest_path()
        self.file_type = self._check_file_type() 
        self.dest_already_symlink = False

    def __repr__(self):
        return f"Symlink({self.src}, {self.dest}"

    def __str__(self):
        return f"""
        Src: {self.src}
        Dest: {self.dest}
        Absolute Src: {self.absolute_src}
        Absolute Dest: {self.absolute_dest}
        Valid Src: {self.valid_src}
        Valid Dest Path: {self.valid_dest_path}
        File Type: {self.file_type}
        Destination Already Symlink?: {self.dest_already_symlink}"""


    def _get_absolute_path(self, item):
        return os.path.expanduser(item)

    def _validate_src(self):
        return os.path.exists(self.absolute_src)

    def _validate_dest_path(self):
        s = self.absolute_dest.split("/")
        s.pop()
        r = "/".join(s) 
        return True

    def _check_file_type(self):
        if os.path.isdir(self.absolute_src):
            return 'directory'
        elif os.path.isfile(self.absolute_src):
            return 'file'
        else:
            logger.error("Error in _check_file_type function")

    def make_paths(self):
        pass

    def simple_create(self):
        os.symlink(self.absolute_src, self.absolute_dest)

    def force_create(self):
        subprocess.call(
                ["ln", "-sfn", f"{self.absolute_src}", 
                    f"{self.absolute_dest}"], 
                shell=True)



