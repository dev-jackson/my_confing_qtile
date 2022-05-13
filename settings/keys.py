
from libqtile.config import Key
from libqtile.command import lazy
from .theme import colors
from .path import qtile_path 

mod = "mod4"

color = colors['active']


keys = [Key(key[0], key[1], *key[2:]) for key in  [


    ([mod], "w", lazy.window.kill()),
    ([mod], "x", lazy.spawn("sh "+qtile_path+"/rofi/bin/powermenu")),
    ([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    ([mod], "d",
        lazy.spawn(
            'dmenu_run -i -fn "Cascadia Code-12" -nb "#000000"  -p "Run"'
        )
     ),
    ([mod], "m", lazy.spawn("sh /home/jackson/.config/qtile/rofi/bin/launcher")),
    ([mod, "shift"], "m", lazy.spawn('rofi-zeal')),
    ([mod], "p", lazy.spawn('pcmanfm')),
    ([mod], "r", lazy.spawn('redshift -O 3500')),
    ([mod], "t", lazy.spawn('telegram-desktop')),
    ([mod], "f", lazy.spawn('firefox-developer-edition --force-device-scale-factor=1.5')),
    ([mod], "c", lazy.spawn('chromium --force-device-scale-factor=1.1')),
    ([mod], "b", lazy.spawn('brave --force-device-scale-factor=1.15')),
    # ([mod], "w", lazy.spawn('whatsapp-nativefier-dark  --force-device-scale-factor=1.2')),

    # Switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # multiple stack panes
    ([mod, "shift"], "Return", lazy.layout.toggle_split()),
    ([mod], "Return", lazy.spawn("kitty")),

    #Nigth
    #([mod, "control"], "n", lazy.spawn('redshift -o')),
    #([mod, "control"], "o", lazy.spawn('redshift -x')),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    #Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    ([], "XF86AudioNext", lazy.spawn("xdotool key XF86AudioNext")),
    ([], "XF86AudioPrev", lazy.spawn("xdotool key XF86AudioPrev")),
    # RESIZE UP, DOWN, LEFT, RIGHT
    ([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    ([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    ([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    ([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    ([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    ([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    ([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    ([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    #SCREENSHOTS
    ([], "Print", lazy.spawn('flameshot full -c')),
    #Key(["shift"], "Print", lazy.spawn('flameshot gui')),
    #Key([mod2, "shift" ], "Print", lazy.spawn('flameshot full -c')),
    #Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),

    # INCREASE/DECREASE BRIGHTNESS
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Toggle floating layout
    ([mod, "shift"], "space", lazy.window.toggle_floating()),

    # Toggle next keyboard layout
    ([mod, "control"], "space", lazy.widget["keyboardlayout"].next_keyboard())
]]
