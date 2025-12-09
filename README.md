<p align="center">
  <a href="https://github.com/priiduneemre/dotfiles">
    <img alt="Dotfiles logo" src="http://nemp.planet.ee/cdn/dotfiles-header-830x200.svg">
  </a>
</p>

<h3 align="center">Priidu's dotfiles</h3>
<p align="center">
  Sensible defaults for common CLI tools and applications
</p>
<hr>

## Philosophy

_"Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."_

This collection of dotfiles aims for simplicity and ease of use.
* Configurations are applied using plain symbolic links.
* Project layout mirrors that of a typical Linux filesystem (for easy mapping).
* Files are kept concise, with docs and unused options removed.

The idea is to symlink only what is needed for a particular setup and ignore the rest. Once
installed, the local repository can be checked periodically for untracked changes (e.g., from OS
package updates). These may then be pushed or reverted accordingly.

## Requirements

Most shell scripts are designed for `zsh`, but will also run fine with `bash`.
Additionally, the `.zshrc` configuration expects [`ohmyzsh`](https://github.com/ohmyzsh/ohmyzsh) to
be installed. This may not fit your workflow, so feel free to adjust accordingly.

DE-specific configurations are primarily aimed at the KDE ecosystem (Konsole, Dolphin, etc.).

## Installation

Just clone the repository and create symbolic links as necessary. For example:

```sh
git clone git@github.com:priiduneemre/dotfiles.git ~/dotfiles

ln -s ~/dotfiles/.zshrc ~/.zshrc
ln -s ~/dotfiles/.editorconfig ~/.editorconfig
ln -s ~/dotfiles/.config/Code/User/settings.json ~/.config/Code/User/settings.json
```

> [!TIP]
> Merge your existing preferences into the dotfiles pulled from the repository. Then, replace the
> original files with symlinks.

## Feedback

Suggestions and ideas welcome. Please open [an issue](https://github.com/priiduneemre/dotfiles/issues)
or submit a [pull request](https://github.com/priiduneemre/dotfiles/pulls).
