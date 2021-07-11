#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
#scrot
nm-applet &
volumeicon &
blueman-applet &
flameshot &
timedatectl set-timezone America/Guayaquil
# feh --bg-fill  + list_wallpapers[num_rand]
#feh --bg-scale /home/jackson/.config/qtile/wallpapers/landscape-colorful-pagoda-1555415.jpg
sudo -S <<<'dev537'  ntpd -qg &
netctl-auto enable-all &
cbatticon -u 5 &
#picom &
python3 ~/.config/qtile/wallpapers/random_wallpaper.py &
picom --experimental-backends &
#dunst &
#run cbatticon &
#numlockx
