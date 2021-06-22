#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run nm-applet &
run volumeicon &
blueman-applet &
#dunst &
#run cbatticon &
#numlockx
