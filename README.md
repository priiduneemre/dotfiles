<p align="center">
  <a href="https://github.com/priiduneemre/dotfiles">
    <img alt="Dotfiles logo" src="http://nemp.planet.ee/cdn/dotfiles-logo-890x640.png" width="295">
  </a>
</p>

<h3 align="center">Nemp's dotfiles</h3>
<p align="center">
  Sensible defaults for common CLI tools and applications
</p>

## Philosophy

This set of dotfiles is designed for simplicity and ease of use.
* Configurations are applied using plain symbolic links.
* Project structure mirrors that of a typical Linux setup (immediately clear where everything goes).
* Files are kept as brief as possible, with no "might need that later" filler.

The idea is to symlink only what is needed for a particular setup and ignore the rest. The local
repository can be periodically checked for external changes (e.g. OS package updates), which may
then be pushed or reverted accordingly.

## Requirements

The shell scripts are designed for `zsh`, but most should also work fine with `bash`.
Additionally, the `.zshrc` configuration expects [`ohmyzsh`](https://github.com/ohmyzsh/ohmyzsh) to
be installed. This may not suit your workflow, so feel free to redact accordingly.

DE-specific configurations primarily target the KDE ecosystem (Konsole, Dolphin, etc.).

## Installation

Just clone the repository to your home directory and symlink what you need:

```sh
git clone git@github.com:priiduneemre/dotfiles.git ~/dotfiles

ln -s ~/dotfiles/.zshrc ~/.zshrc
ln -s ~/dotfiles/.editorconfig ~/.editorconfig
ln -s ~/dotfiles/.config/Code/User/settings.json ~/.config/Code/User/settings.json
```

**Note:** you should incorporate your own preferences first, then replace the original files with
the symlinks.

## Feedback

Suggestions and ideas welcome. Please open [an issue](https://github.com/priiduneemre/dotfiles/issues)
or submit a [pull request](https://github.com/priiduneemre/dotfiles/pulls).
