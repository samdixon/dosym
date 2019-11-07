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

def add_symlinks_helper2(processed_input_data) -> list: 
    l = list()
    for key, val in processed_input_data.localpath_symlinks.items():
        l.append(Symlink(key,val))
        logger.debug(f"Adds {key}: {val} to Symlinks List")

    return l


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
            try:
                os.symlink(os.path.expanduser(key), os.path.expanduser(val))
            except FileNotFoundError as e:
                pass
            except FileExistsError as e:
                pass
            
class Symlink():
    """Class to create a single instance of a Symlink"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.absolute_src = self._get_absolute_path(self.src)
        self.absolute_dest = self._get_absolute_path(self.dest)
        self.valid_src = self._validate_src()
        self.valid_dest_path = self._validate_dest_path()

    def __repr__(self):
        return f"Symlink({self.src}, {self.dest}")

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



