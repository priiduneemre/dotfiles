#!/bin/bash

ZSHRCD_DIR="$HOME/.zshrc.d"

# Source all runcommands from `~/.zshrc.d` in alphabetical order
[[ -d "$ZSHRCD_DIR" ]] || return

for runcmd in "$ZSHRCD_DIR"/*; do
  [[ -f "$runcmd" && -r "$runcmd" ]] || continue
  source "$runcmd"
done
unset runcmd
