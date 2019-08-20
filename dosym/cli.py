# cli
# code related to the CLI portion of this application
import argparse
import sys
import logging
from dosym import symlink
from dosym import inputdata
import toml

logger = logging.getLogger(__name__)
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
    parser.add_argument("-d", "--debug", help="Enable Debug", action="store_true")
    args = parser.parse_args()
    return args

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
def gather_inputs(args: argparse.Namespace) -> dict:
    if args.files:
       # TODO Error handling and logging for non TOML files
       input_data = toml_file_parser(args.files[0])

       logger.debug(input_data)
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
        input_data = toml_stdin_parser()
        logger.debug(input_data)
    
    return input_data

  # TODO put if elif else statement from cli in here

#Main control flow function of CLI module"
def cli():
    # create argument parser && parse args
    args = create_parser()

    if args.debug:
        logging.basicConfig(filename="debug.log", level=logging.DEBUG, format='%(asctime)h %(levelname)-8s %(name)s: %(message)s')
    else:
        logging.basicConfig(level=logging.INFO)

    logger.debug("Argparse Namespace: " + str(args))

    # gather input from stdin or file
    input_data = gather_inputs(args)

    # create instance of input data processor class which auto
    # sanitizers (maybe rename this to input sanitizer (look it up)
    # and gets it ready to dispatch to other classes for work to be done
    processed_input_data = inputdata.InputDataTransformer(
                                    input_data['symlinks'], 
                                    input_data['optional'])

    logger.debug(processed_input_data)

    # Instantiate empty symlink data structure
    # which holds information on symlinks to be added
    # may rename this to something like 
    # SymlinkFactory (look it up on terminology)
    symlink_object = symlink.Symlinks()

    # TODO 
    # Move this to input processing class
    # This needs to be an if statement:
    # If localpath = True: Merge localpath and key
    # Else key is just based off relative path
    # First option will be preferred. Second will require tons of error
    # handling and boilerplate code
    for key,val in processed_input_data.localpath_symlinks.items():
        symlink_object.add_symlink(key,val)
        
    print(symlink_object.validated_symlinks)

    symlink_object.create_symlinks()
    sys.exit(0)


    

