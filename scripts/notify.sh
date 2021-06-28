#!/bin/bash

if zenity --question --width="250" --title="Information" --text="\n You want to shut down the computer?"
then 
    sudo -S <<< "dev537" shutdown -h 0
else 
    echo "No"
fi