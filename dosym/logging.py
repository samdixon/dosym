import logging

# TODO
# Format logging strings
def create_cli_logger():
    logger = logging.getLogger("cli")
    logging.basicConfig(filename="main.log", level=logging.DEBUG)
    return logger

def create_symlink_logger():
    logger = logging.getLogger("symlink")
    logging.basicConfig(filename="main.log", level=logging.DEBUG)
    return logger

