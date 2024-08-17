#!/bin/bash

# Custom shell functions for CLI productivity

function cs() {
  cd "$1" && ls -la
}

function dh() {
  dolphin --select "$1"
}

function ofv() {
  sudo openfortivpn -c "/etc/openfortivpn/${1}" --use-resolvconf=1
}

function precmd() {
  echo -ne "\033]0;${PWD/#$HOME/~}\007"
}

function ssha() {
  ssh-add "$HOME/.ssh/${1}"
}

function udd() {
  udisks --detach "/dev/${1}"
}

function wreq() {
  dnf repoquery -i -q --installed --whatrequires "$1"
}
