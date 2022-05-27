#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

killall -9 xsettingsd dunst xfce4-power-manager 

lxsession &
nm-applet &
volumeicon &
blueman-applet &
flameshot &
timedatectl set-timezone America/Guayaquil
cbatticon -u 5 &
gnome-keyring-daemon &
feh --bg-scale --randomize ~/.config/qtile/wallpapers/* 
#touchegg &
#python3 ~/.config/qtile/wallpapers/random_wallpaper.py &
picom --config $HOME/.config/qtile/scripts/picom.conf  &
udiskie &
#xsettingsd &

if [[!`pidof xfce-polkit`]]; then
  /usr/lib/xfce-polkit/xfce-polkit
fi

dunst -conf ~/.config/qtile/scripts/dunstrc &
xfce4-power-manager &
betterlockscreen -u /home/jackson/.config/qtile/wallpapers
