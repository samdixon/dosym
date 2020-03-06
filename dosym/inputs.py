import sys
import logging
import toml
import dosym.exceptions as exceptions

logger = logging.getLogger(__name__)

class InputData(object):
    """Transforms input data. Joins paths and creates data structures"""
    def __init__(self, input_data):
        self.input_data = input_data
        self.symlinks = None
        self.optional = None
        self.git_remote = None 
        self.source_prefix = None
        self.localpath_symlinks = None

        if 'symlinks' in self.input_data:
            self.symlinks = self.input_data['symlinks']
        if 'optional' in self.input_data:
            self.optional = self.input_data['optional']
            self._parse_optional_inputs()
        
        if self.source_prefix != None:
            self._join_source_prefix_and_key()
        else:
            self.localpath_symlinks = self.symlinks
    
    def __repr__(self):
        return f"InputData({self.input_data})"

    def __str__(self):
        return f"""
        symlinks: {self.symlinks}
        optional: {self.optional}
        git_remote: {self.git_remote}
        source_prefix: {self.source_prefix}
        localpath_symlinks: {self.localpath_symlinks}"""

    def _parse_optional_inputs(self):
        if 'git_remote' in self.optional:
            self.git_remote = self.optional['git_remote']
        if 'source_prefix' in self.optional:
            self.source_prefix = self.optional['source_prefix']

    def determine_path_type(self):
        pass

    def _join_source_prefix_and_key(self):
        self.localpath_symlinks = {}
        for key,val in self.symlinks.items():
            if key.startswith("!"):
                new_key = key.lstrip("!")
                self.localpath_symlinks[new_key] = val
            else:
                join_char = "/"
                join_seq = (self.optional['source_prefix'], key)
                joined_key = join_char.join(join_seq)
                self.localpath_symlinks[joined_key] = val

def toml_file_parser(inputfiles):
    return toml.load(inputfiles)

def toml_stdin_parser():
    if len(sys.stdin.readlines()) == 0:
        raise exceptions.BlankFileError
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
        except exceptions.BlankFileError as e:
            print("Blank File")
            exit()
            
    
    return input_data


def process(args) -> InputData:
    raw = gather_inputs(args)
    parsed = InputData(raw)
    logger.debug(f'Proccessed input data: {parsed}')

    return parsed


