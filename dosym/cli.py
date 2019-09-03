# cli
# code related to the CLI portion of this application
import argparse
import sys
import logging
import dosym.symlinks as symlinks
import dosym.inputs as inputs

logger = logging.getLogger(__name__)
logger.info("---------------------------------")


def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            description="Dosym. Easily create and remove symbolic links.")
    parser.add_argument(
            "files", 
            metavar="FILE", 
            nargs="*", 
            help="One or more config files")
    parser.add_argument("-d", "--debug", help="Enable Debug", action="store_true")
    args = parser.parse_args()
    return args


# Main control flow function of CLI module
def cli() -> int:
    args = create_parser()

    if args.debug:
        logging.basicConfig(filename="debug.log", level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logger.debug("Argparse Namespace: " + str(args))

    # gather input from stdin or file
    input_data = inputs.gather_inputs(args)

    """
    Create instance of InputDataTransformer class which transforms
    input_data into useable form for other classes
    """
    processed_input_data = inputs.InputDataTransformer(
                                    input_data['symlinks'], 
                                    input_data['optional'])

    # TODO
    # Update repr for this logger so it looks nice
    logger.debug('Proccessed input data: {}'.format(processed_input_data))

    # Instantiate empty Symlinks class
    symlink_object = symlinks.Symlinks()

    symlinks.add_symlinks_helper(symlink_object, processed_input_data)
        
    if (len(symlink_object.validated_symlinks.items()) > 0):
        symlink_object.create_symlinks()
    else:
        # TODO
        # Exception
        print("No symlinks given")

    ## This needs to be either in the symlinks class or in some
    ## other func
    print("Successfully created the following symlinks:")
    for key,val in symlink_object.validated_symlinks.items():
        print(key, "-->\t", val)


    return 0

    

