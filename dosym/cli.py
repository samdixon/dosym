import argparse
import sys
import logging
import dosym.symlinks as symlinks
import dosym.inputs as inputs

logger = logging.getLogger(__name__)

def create_parser(optional=None):
    parser = argparse.ArgumentParser(
            description=
            "Dosym. Easily create and remove symbolic links with a toml file.")
    parser.add_argument(
            "files",
            metavar="FILE",
            nargs="*",
            help="One or more config files")
    parser.add_argument(
            "-f",
            "--force",
            help="Force create symlink and overlink current files",
            action="store_true"
            )
    parser.add_argument(
            "-d", 
            "--debug", 
            help="Enable Debug", 
            action="store_true")
    args = parser.parse_args(optional)
    return args

def check_debug_mode(args):
    if args.debug:
        debug_file = "debug.log"
        print(f"Writing debug log to ./{debug_file}")
        logging.basicConfig(filename=debug_file, level=logging.DEBUG)
        logger.debug("\nDebug Logging Begin\n")
        return True 
    else:
        logging.basicConfig(level=logging.INFO)
        return False 

def cli():
    args = create_parser()
    check_debug_mode(args)

    processed_input_data = inputs.process(args)

    symlinks = symlinks.add_symlinks_helper(processed_input_data)

    print("Created the following symlinks:")
    for link in symlink_list:
        if link.is_valid_src:
            link.create(args.force)
        else:
            print("Link src not valid")
    return 0



