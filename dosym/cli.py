# cli
# code related to the CLI portion of this application
import argparse
import sys
from dosym import logging
from dosym import symlink
import toml

logger = logging.create_cli_logger()
logger.info("----")
logger.info("CLI logger successfully created")
logger.info("----")


def create_parser():
    parser = argparse.ArgumentParser(description="Dosym. Easily create and remove symlinks")
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

def file_parser(inputfiles):
    return toml.load(inputfiles)

def process_inputs():
    # TODO put if elif else statement from cli in here
    pass

"Main control flow function of CLI module"
def cli():
    args = create_parser()

    logger.debug("Logging Args")
    logger.debug(args)

    if args.files:
        # TODO Error handling and logging for non TOML files
        input_file_data = file_parser(args.files[0])

        logger.debug(data)
        logger.debug("args.files true")
    elif sys.stdin.isatty():
        exit()
    else:
        temp = ""
        for line in sys.stdin:
            temp += line

        input_file_data = toml.loads(temp)

        logger.debug(input_file_data)

    ConfigInputs = ConfigFileInputs(
            input_file_data['symlinks'], 
            input_file_data['optional'])

    logger.debug(ConfigInputs)

    symlink_object = symlink.DoSymlinks()
    for key,val in ConfigInputs.symlinks.items():
        symlink_object.add_symlink(key, val)

    print(symlink_object.symlinks)



    

