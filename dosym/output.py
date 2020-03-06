class Terminal(object):
    pass


class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Outputs(Terminal):
    def __init__(self, symlinks):
        self.symlinks = symlinks

    def symlink_output(self):
        for symlink in self.symlinks:
            if symlink.status == symlink.CREATED:
                color = tcolors.OKGREEN
            elif symlink.status == symlink.BROKEN:
                color = tcolors.WARNING
            elif symlink.status == symlink.FAILED:
                color = tcolors.FAIL
            print(
                    "[" + 
                    color + 
                    f"{symlink.status}" + 
                    tcolors.ENDC +
                    "]",
                    f"{symlink.src} -> {symlink.dest}")
            
            if symlink.status == symlink.BROKEN:
                print("    - Warning: Symlink created, but source file does not exist")


