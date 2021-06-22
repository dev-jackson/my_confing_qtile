# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import random as rnd
import subprocess

mod = "mod4"
home = os.path.expanduser('~')
#terminal = guess_terminal()
#terminal = "lxterminal"
#terminal  = "alacritty"
terminal = "tilix"
keys = [
    Key([mod], "q", lazy.window.kill()),

    Key([mod], "d", lazy.spawn('dmenu_run -i -fn "Cascadia Code-12" -nb "#000000" -sb "#2e86c1" -p "Run"')),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    #Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer -c 1 -q set Master 2dB+')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer -c 1 -q set Master 2dB-')),
    
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    #SCREENSHOTS
    Key([], "Print", lazy.spawn('flameshot full -c')),
    #Key([mod2, "shift" ], "Print", lazy.spawn('flameshot full -c')),
    #Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),

]

#groups = [Group(i) for i in "123"]
__groups = {
    1: Group("DEV"),
    2: Group("WEB"),
    3: Group("MEDIA")
}
groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend((
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen()),

        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
        )
    ))

def init_layout_teme():
    return {
        "margin": 5,
        "border_with": 2,
        "border_focus": "#2e86c1",
        "border_normal": "#999999"
    }    

layout_theme = init_layout_teme()

def init_colors():
    return [
            ["#17a589", "#17a589"],
            ["#2e86c1", "#2e86c1"],
            ["#999999", "#999999"],
            ["#ffffff", "#ffffff"],
            ["#000000", "#000000"]
            ]

colors = init_colors()


layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    layout.Stack(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#def shutdown_btn():
#    result = question(title="Question",text="Shutdown yout pc?\nAutomatly shutdown 60 secons",timeout=60)
#    print(result)

widget_defaults = dict(
    font='Fira Code',
    fontsize=12,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 1,
                    padding = 10
                ),
                widget.Image(
                    filename = "~/.config/qtile/icons/arch_icon.png",
                    iconsize = 1,
                    padding = 5,
                    mouse_callbacks = {
                    'Button1' : lambda : qtile.cmd_spawn(
                            'dmenu_run -i -fn "Cascadia Code-13" -nb "#000000" -sb "#2e86c1" -p "Run"'
                        )
                    }
                ),
                widget.Sep(
                    linewidth =1,
                    padding = 10,
                ),
                widget.GroupBox(
                    font = "Cascadia Code Bold",
                    fontsize = 12,    
                    padding_y = 6,
                    padding_x = 8,
                    borderwidth = 0,
                    disable_drag = False,
                    active = colors[3],
                    inactive = colors[2],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors[1],
                    foreground = colors[0],
                    background = colors[4]
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 10
                ),
                # widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    padding = 5,
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text = '',
                    background = colors[4],
                    foreground = colors[1],
                    padding = 0,
                    fontsize = 18
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons/")],
                    background = colors[1],
                    padding = 0,
	                scale = 0.7
                ),
                widget.CurrentLayout(
                    font="Cascadia Code Bold",
                    padding = 5,
                    background=colors[1]
                ),
                widget.TextBox(
                    text = '',
                    background = colors[1],
                    foreground = colors[0],
                    padding = 0,
                    fontsize = 18
                ),
                widget.TextBox(
                    font="FontAwesome",
                    text="  ",
                    foreground=colors[3],
                    background=colors[0],
                    padding = 0,
                    fontsize=18
                ),
                widget.Memory(
                    font="Cascadia Code Bold",
                    format='{MemUsed}M/{MemTotal}M',
                    update_interval = 1,
                    padding = 5,
                    font_size = 12,
                    background = colors[0],
                    foreground = colors[3],
                ),
                widget.TextBox(
                    text = '',
                    background = colors[0],
                    foreground = colors[1],
                    padding = 0,
                    fontsize = 18
                ),
                widget.CPU(
                    font="Cascadia Code Bold",
                    padding = 5,
                    update_interval = 1,
                    foreground = colors[3],
                    background = colors[1]
                ),
                # widget.Volume(
                #     fontsize=10, 
                #     update_interval=2,
                #     volume_app="pamixer"),
                widget.TextBox(
                    text = '',
                    background = colors[1],
                    foreground = colors[0],
                    padding = 0,
                    fontsize = 18
                ),
                widget.TextBox(
                    font = "Cascadia Code Bold",
                    text = '⌚',
                    background = colors[0],
                    foreground = colors[3],
                    padding = 0,
                    font_size = 18
                ),
#                widget.Net(
#                    font="Cascadia Code",
#                    fontsize=12,
#                    interface=["wlp7s0"]
#                ),
                #widget.Wlan(
                #    font="Cascadia Code",
                #    interface=["wlp7s0"],
                #    update_interval=1,
                #    mouse_callbacks = {
                #        'Button1': lambda : qtile.cmd_spawn(terminal + '-e sudo wifi-menu')
                #    }
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Clock(
                    font="Cascadia Code Bold",
                    format='%A, %B %d - %H:%M',
                    background = colors[0],
                    padding = 5
                ),
                 widget.TextBox(
                    text = '',
                    background = colors[0],
                    foreground = colors[1],
                    padding = 0,
                    fontsize = 18
                ),
                #widget.QuickExit(),
                widget.Systray(
                    padding = 5,
                    background = colors[1]
                ),
                widget.Sep(
                    linewidth = 2,
                    background = colors[1],
                    foreground = colors[1]
                ),
                widget.TextBox(
                    text = '',
                    background = colors[1],
                    foreground = colors[3],
                    padding = 0,
                    fontsize = 18
                ),
                widget.Image(
                    filename = "~/.config/qtile/icons/power-button.svg",
                    background = colors[3],
                    margin = 2,
                    iconsize = 5,
                    foreground = colors[3],
                    mouse_callbacks = {
                    'Button1' : lambda : qtile.cmd_spawn('sh '+home + '/.config/qtile/scrips/notify.sh')
                    }
                ),
            ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),  # GPG key password entry
])

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


def get_path_ramdon_wallpaper():
    return os.listdir('/home/jackson/.config/qtile/wallpapers/')

list_wallpapers = get_path_ramdon_wallpaper()
num_rand = rnd.randint(0,(len(list_wallpapers) -1))



auto_start = [
    "loadkeys us",
    "timedatectl set-timezone America/Guayaquil",
    "feh --bg-fill /home/jackson/.config/qtile/wallpapers/"+ list_wallpapers[num_rand] +" &"
    "sudo -S <<<'dev537'  ntpd -qg",
    "nm-applet &",
    "netctl-auto enable-all",
    #"flameshot"
]

for x in auto_start:
    os.system(x)

