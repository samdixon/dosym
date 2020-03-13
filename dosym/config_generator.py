import os.path
import sys
import toml


config_file = "./symlinks.toml"
base = """[symlinks]
# Format:  
# 'source' = 'destination'
# Add your symlinks below this line

[optional]
# Source prefix for prepending to symlink source
# eg: source_prefix = '~/code'
#     all dotfiles will add '~/code' to front
source_prefix = '' 
# Http remote git address for pulling git files
git_remote = ''
"""

def validate_toml():
    try:
        toml_string = toml.loads(base)
    except Exception as e:
        print(e)
        sys.exit(1)

def generate():
    validate_toml()

    if not os.path.isfile(config_file):
        try:
            with open(config_file, 'w') as f:
                f.writelines(base)
                sys.stdout.write(
                        "Generated blank config file at ./symlinks.toml\n")
                sys.exit(0)
        except Exception as e:
            sys.stderr.write(f"{e}\n")
            sys.exit(1)
    else:
        sys.stderr.write("Config file already exists at ./symlinks.toml\n")
        sys.exit(1)


