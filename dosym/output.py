class Terminal(object):
    check = u'\u2714' 
    error = u'\u2715'
    broken = u'\u2718'
    arrow = u'\u21D2'
    broken_arrow = u'\u21CF'
    under_arrow = u'\u21AA'


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
        super().__init__()

    def symlink_output(self):
        for symlink in self.symlinks:
            arrow = self.arrow
            if symlink.status == symlink.CREATED:
                color = tcolors.OKGREEN
                status = self.check
            elif symlink.status == symlink.BROKEN:
                color = tcolors.WARNING
                status = self.broken
                arrow = self.broken_arrow
            elif symlink.status == symlink.FAILED:
                color = tcolors.FAIL
                status = self.error
            print(
                    "[" + 
                    color + 
                    f"{status}" + 
                    tcolors.ENDC +
                    "]",
                    f"{symlink.src} " + 
                    arrow +
                    f" {symlink.dest}")
            
            if symlink.status == symlink.BROKEN:
                print(f"  {self.under_arrow} Warning: Symlink created, but source file does not exist")
            elif symlink.status == symlink.FAILED:
                print(f"  - {symlink.error_message}")


