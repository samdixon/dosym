# Dosym

Dosym is a program that creates symlinks based off the input of a toml configuration file. It can also accept a toml file via stdin. This can be useful as you may specify a `git_remote` url that will pull the files down.

### Example Usage

Run with a file specified
`dosym symlinks.toml`

Run via stdin pipe
`curl https://raw.githubusercontent.com/samdixon/dotfiles/master/symlinks.toml | dosym`

### Toml File Layout
The file uses standard toml formatting. Below is a good reference for what the file should look like:

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



