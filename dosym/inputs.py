import sys
import logging
import toml

logger = logging.getLogger(__name__)

def toml_file_parser(inputfiles: str) -> dict:
    return toml.load(inputfiles)

class BlankFileError(Exception):
    # TODO Move to Exception File
    """Raised when stdin input file doesn't exist or is blank"""
    pass

def toml_stdin_parser() -> dict:
    if len(sys.stdin.readlines()) == 0:
        raise BlankFileError
    buf = ""
    for line in sys.stdin:
        buf += line

    return toml.loads(buf)

# Function to gather inputs based on type
# If file -> toml_file_parser
# If stdin -> toml_stdin_parser()
def gather_inputs(args) -> dict:
    if args.files:
       try:
           input_data = toml_file_parser(args.files[0])
           logger.debug("File Input Data: {}".format(input_data))
       except toml.decoder.TomlDecodeError as e:
           print("TomlDecodeError from input file")
           print(f"Error: {e}")
           print("Exiting...")
           sys.exit()
       except FileNotFoundError as e:
            print("FileNotFound Error")
            print(f"Error: {e}")
            print("Exiting...")
            sys.exit()
    elif sys.stdin.isatty():
        print("No input file given and no input received")
        print("Exiting")
        sys.exit()
    else:
        try:
           input_data = toml_stdin_parser()
           logger.debug("Stdin Input Data: {}".format(input_data))
        except toml.decoder.TomlDecodeError as e:
           print("TomlDecodeError from input file")
           print(f"Error: {e}")
           print("Exiting...")
           sys.exit()
        except BlankFileError as e:
            print("Blank File")
            exit()
            
    
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


