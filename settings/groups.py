from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

groups = [Group(i) for i in [
    "  ", " ", " ", " ", " "
]]

for i, group in enumerate(groups):
    now_key = str(i + 1)
    keys.extend([
        Key([mod], now_key, lazy.group[group.name].toscreen()),

        Key([mod, "shift"], now_key, lazy.window.togroup(group.name))
    ])
