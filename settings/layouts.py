
from libqtile import layout
from libqtile.config import Match
from .theme import colors


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 2,
    'margin': 8
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Columns(**layout_conf),
    layout.Max(),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(**layout_conf),
    layout.RatioTile(**layout_conf),
    layout.Floating(**layout_conf)
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry')
    ],
    border_focus=colors["color4"][0]
)
