import os
import random as rdm



wallpapers = []
for file in os.listdir("/home/jackson/.config/qtile/wallpapers/"):
    if file.endswith(tuple([".png",".jpg",".jpge"])):
        wallpapers.append(
            os.path.join("/home/jackson/.config/qtile/wallpapers/",file)
        )

ramdon_num = rdm.randint(0,(len(wallpapers)-1))

print(wallpapers)
os.system("feh --bg-scale "+wallpapers[ramdon_num]+"")
