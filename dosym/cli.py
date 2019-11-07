import argparse
import sys
import logging
import dosym.symlinks as symlinks
import dosym.inputs as inputs

logger = logging.getLogger(__name__)

def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            description=
            "Dosym. Easily create and remove symbolic links.")
    parser.add_argument(
            "files",
            metavar="FILE",
            nargs="*",
            help="One or more config files")
    parser.add_argument(
            "-d", 
            "--debug", 
            help="Enable Debug", 
            action="store_true")
    args = parser.parse_args()
    return args


# Main control flow function of CLI module
# Code starts and ends here.
def cli() -> int:
    args = create_parser()
    if args.debug:
        logging.basicConfig(filename="debug.log", level=logging.DEBUG)
        logger.debug("\nDebug Logging Begin\n")
    else:
        logging.basicConfig(level=logging.INFO)

    # Fix this messing concat
    logger.debug("Argparse Namespace: " + str(args))

    input_data = inputs.gather_inputs(args)

    processed_input_data = inputs.InputDataTransformer(input_data)
    logger.debug('Proccessed input data: {}'.format(processed_input_data))

    symlink_list = symlinks.add_symlinks_helper2(processed_input_data)
    logger.debug(f"Symlink_List: {symlink_list}")
    for i in symlink_list:
        logger.debug(f"{i}")
    exit()

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



