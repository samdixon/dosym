# cli
# code related to the CLI portion of this application
import argparse
import sys
from dosym import logging
from dosym import symlink
import toml

logger = logging.create_cli_logger()
logger.info("////////////////////////////////")
logger.info("Start of new run")
logger.info("////////////////////////////////")


def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            description="Dosym. Easily create and remove symlinks")
    parser.add_argument(
            "files", 
            metavar="FILE", 
            nargs="*", 
            help="One or more config files")
    parser.add_argument(
            "--git", 
            type=str,
            help="Git destination address")
    args = parser.parse_args()
    return args

class ConfigFileInputs:
    def __init__(self, symlinks, localpath):
        self.symlinks = symlinks
        self.localpath = localpath

def toml_file_parser(inputfiles: str) -> dict:
    return toml.load(inputfiles)

def toml_stdin_parser() -> dict:
    temp = ""
    for line in sys.stdin:
        temp += line

    input_file_data = toml.loads(temp)
    return input_file_data

# Function to process inputs base on Input Type
# If file input -> toml_file_parser
# If stdin input -> toml_stdin_parser
def process_inputs(args: argparse.Namespace) -> dict:
    if args.files:
       # TODO Error handling and logging for non TOML files
       input_file_data = toml_file_parser(args.files[0])

       logger.debug(input_file_data)
       logger.debug("args.files true")
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
        input_file_data = toml_stdin_parser()
        logger.debug(input_file_data)
    
    return input_file_data

  # TODO put if elif else statement from cli in here

#Main control flow function of CLI module"
def cli():
    args = create_parser()

    logger.debug("Logging Args")
    logger.debug(args)

    input_file_data = process_inputs(args)

    ConfigInputs = ConfigFileInputs(
            input_file_data['symlinks'], 
            input_file_data['optional'])

    logger.debug(ConfigInputs)

    symlink_object = symlink.DoSymlinks()

    # TODO 
    # This needs to be an if statement:
    # If localpath = True: Merge localpath and key
    # Else key is just based off relative path
    # First option will be preferred. Second will require tons of error
    # handling and boilerplate code
    for key,val in ConfigInputs.symlinks.items():
        join_char = "/"
        join_seq = (ConfigInputs.localpath['local_source'], key)
        joined_key = join_char.join(join_seq)
        symlink_object.add_symlink(joined_key, val)

    print(symlink_object.symlinks)



    

