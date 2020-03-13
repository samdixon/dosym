import argparse
import sys
import logging
import dosym.symlinks as symlinks
import dosym.config_generator as config_generator
import dosym.inputs as inputs
import dosym.output as output

__version__ = '0.0.3'
logger = logging.getLogger(__name__)

def create_parser(optional=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            description=
            "dosym - quickly & easily create symlinks with a toml file.")
    parser.add_argument(
            "files",
            metavar="file",
            nargs="*",
            help="one or more config files")
    parser.add_argument(
            "-f",
            "--force",
            help="force create symlink over any current files",
            action="store_true"
            )
    parser.add_argument(
            "-d", 
            "--debug", 
            help="enable debug logging", 
            action="store_true")
    parser.add_argument(
            "--generate-config",
            help="generate a blank config file in current directory",
            action="store_true"
            )
    parser.add_argument(
            "--version",
            help="print dosym version",
            action="store_true"
            )
    args = parser.parse_args(optional)
    return args

def check_debug_mode(args: argparse.Namespace) -> bool:
    if args.debug:
        debug_file = "debug.log"
        print(f"Writing debug log to ./{debug_file}")
        logging.basicConfig(filename=debug_file, level=logging.DEBUG)
        logger.debug("\nDebug Logging Begin\n")
        return True 
    else:
        logging.basicConfig(level=logging.INFO)
        return False 

def check_generate_config_flag(args: argparse.Namespace) -> None:
    if args.generate_config:
        generate_config_file(args)

def generate_config_file(args: argparse.Namespace) -> None:
    config_generator.generate()

def check_version_flag(args: argparse.Namespace) -> None:
    if args.version:
        print(__version__)
        sys.exit(0)

def main() -> int:
    args = create_parser()
    check_debug_mode(args)
    check_generate_config_flag(args)
    check_version_flag(args)


    input_data = inputs.process(args)

    symlink_list = symlinks.add_symlinks_helper(input_data)

    for link in symlink_list:
        link.create(args.force)

    outputs = output.Outputs(symlink_list) 
    outputs.symlink_output()
    return 0



