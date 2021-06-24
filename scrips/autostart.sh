#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

nm-applet &
volumeicon &
blueman-applet &
flameshot &
#dunst &
#run cbatticon &
#numlockx
