# Symlink Class File
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

"""
Simple helper function that adds symlinks to Symlinks class
"""
def add_symlinks_helper(processed_input_data) -> list: 
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
        Valid Dest Path: {self.valid_dest_path}"""

    def _get_absolute_path(self, item) -> bool:
        return os.path.expanduser(item)

    def _validate_src(self) -> bool:
        return os.path.exists(self.absolute_src)

    def _validate_dest_path(self) -> bool:
        s = self.absolute_dest.split("/")
        s.pop()
        r = "/".join(s) 
        print(os.path.exists(r))
        print(r)
        return True

    def make_paths(self):
        pass

    def simple_create(self):
        os.symlink(self.absolute_src, self.absolute_dest)

    def force_create(self):
        subprocess.call(
                ["ln", "-sfn", f"{self.absolute_src}", 
                    f"{self.absolute_dest}"], 
                shell=True)



