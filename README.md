# Dosym

Dosym is a way to quickly & easily create symlinks with a toml file.

### Example Usage

Run with a file specified

```
dosym symlinks.toml
```

Run via stdin pipe
* this can be useful with the 'git_remote' option set as dosym will automatically pull in your files if needed.

```
curl https://raw.githubusercontent.com/samdixon/dotfiles/master/symlinks.toml | dosym
```

### Toml Config File 
Dosym determines what links need to be created by giving the program a toml configuration file. A starter configuration file can be generated with the following command:

```
dosym --generate-config
```

A completed dosym file might look like the following:
```
[symlinks]
# Format:
# 'source' = 'destination'
"npmrc" = "~/.npmrc"
'vimrc' = '~/.vimrc'
'inputrc' = '~/.inputrc'
'alacritty.yml' = '~/.config/alacritty/alacritty.yml'
'init.vim' = '~/.config/nvim/init.vim'
'bashrc' = '~/.bashrc'
'bash_files' = '~/.bash_files'
'gitconfig' = '~/.gitconfig'

[optional]
source_prefix = "~/code/dotfiles"
git_remote = 'https://github.com/samdixon/dotfiles'
```

Symlinks are formatted in the form of Src -> Dest. The `source_prefix` optional variable allows you to set a prefix path for the symlink files. This is useful if you dotfiles aren't in your current path. If a symlink needs to ignore this setting, prefix the source with a `!`.

`git_remote` will pull down the git repository to the `source_prefix` if specified, otherwise it will default to your current path. This feature will be release in the future.


### Installation
Currently there is no active installation candidate. The file can be installed via running `python3 setup.py install`

### Contributing
Contributing is welcomed. The goal of the project is to simply create symlinks. Anything that improves the output, programming style, testing, documentation, or data structures is welcome. Additional feature requests can be discussed.

### License
MIT



