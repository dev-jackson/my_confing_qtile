from libqtile import widget
from .theme import colors

def base_color(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base_color(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base_color(fg=fg,bg=bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def powerline(fg='light',bg='dark'):
    return widget.TextBox(
        **base_color(fg=fg,bg=bg),
        text="",
        fontsize=52,
        padding=-9
    )

def workspaces():
    return [
        separator(),
        icon(text='' ,fontsize=30,fg='light'),
        separator(),
        widget.GroupBox(
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=8,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(),
        separator()
    ]

primary_widgets = [
    *workspaces(),
    separator(),
    powerline("color4", "dark"),
    icon(bg="color4",fg='light', text=''),
    widget.CheckUpdates(
        font="Cascadia Code Bold",
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_update=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates'
    ),
    powerline('color3','color4'),
    icon(bg='color3', fg='light',text=''),
    widget.Net(
        **base_color(bg='color3', fg='light'),
        font="Cascadia Code Bold",
        interface='wlp7s0'
    ),
    powerline('color2', 'color3'),
    widget.CurrentLayoutIcon(
        **base_color(bg='color2'),
        font="Cascadia Code Bold",
        scale=0.70
    ),
    widget.CurrentLayout(
        **base_color(bg='color2',fg='light'), 
        font="Cascadia Code Bold",
        padding=5
    ),
    powerline('color1', 'color2'),
    icon(bg="color1", fg='light' ,fontsize=17, text=''),
    widget.Clock(
        **base_color(bg='color1', fg='light'),
        font="Cascadia Code Bold",
        format='%d/%m/%Y - %H:%M '
    ),
    powerline('dark','color1'),
    widget.Systray(
        background=colors['dark'],
        padding=5
    )
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base_color(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base_color(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base_color(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widgets_default = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1
}

extension_defaults = widgets_default.copy()