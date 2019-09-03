import sys
import logging
import toml

logger = logging.getLogger(__name__)

def toml_file_parser(inputfiles: str) -> dict:
    return toml.load(inputfiles)

def toml_stdin_parser() -> dict:
    temp = ""
    for line in sys.stdin:
        temp += line

    return toml.loads(temp)

# Function to gather inputs based on type
# If file -> toml_file_parser
# If stdin -> toml_stdin_parser()
def gather_inputs(args) -> dict:
    if args.files:
       # TODO Error handling and logging for non TOML files
       input_data = toml_file_parser(args.files[0])

       logger.debug("File Input Data: {}".format(input_data))
    elif sys.stdin.isatty():
        # TODO 
        # Error handling around no input given
        # throw error, exit, let user know why
        print("No input file given and no input received")
        print("Exiting")
        exit()
    else:
        # TODO
        # error handling around this?
        # what if input from stdin is not proper toml
        # Throw error, exit, let user know why
        # Log and throw error
        input_data = toml_stdin_parser()
        logger.debug("Stdin Input Data: {}".format(input_data))
    
    return input_data

class InputDataTransformer:
    def __init__(self, symlinks, optional):
        self.symlinks = symlinks
        self.optional = optional
        self.git_remote = None 
        self.local_path = None
        self.localpath_symlinks = None

        self._parse_optional_inputs()
        
        if self.local_path != None:
            self._join_local_path_and_key()
    
    def _parse_optional_inputs(self):
        if 'git_remote' in self.optional:
            self.git_remote = self.optional['git_remote']
        if 'local_path' in self.optional:
            self.local_path = self.optional['local_path']

    def determine_path_type(self):
        pass

    def _join_local_path_and_key(self):
        self.localpath_symlinks = {}
        for key,val in self.symlinks.items():
            join_char = "/"
            join_seq = (self.optional['local_path'], key)
            joined_key = join_char.join(join_seq)
            self.localpath_symlinks[joined_key] = val


