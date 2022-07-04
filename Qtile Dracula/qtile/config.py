#QTILE DRACULA

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer
import os
import subprocess

# Startup hook
@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

# Defaults
mod = "mod4"
terminal = "alacritty"

keys = [
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
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Launch dmenu"),
    Key([mod], "p", lazy.spawn("rofi -show run"), desc="Launch rofi"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "c", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    # Lock Computer
    Key([mod, "control"], "m", lazy.spawmcmd("dm-tool lock"), desc="Lock Computer"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #    desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
  #  layout.Columns(border_focus_stack='#fsdfbd'),
    # Try more layouts by unleashing below layouts.
#    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(ratio=0.5, 
                add_on_top=False, 
                border_focus='#bd93f9', 
                border_width=2, margin=6
                ),
    # layout.TreeTab(),
    layout.Max(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

### BAR ###

colors = [["#000000", "#000000"], # 0  black
          ["#ffffff", "#ffffff"], # 1  white
          ["#e4e4e4", "#e4e4e4"], # 2  light gray
          ["#282a36", "#282a36"], # 3  dark gray
          ["#61b1db", "#61b1db"], # 4  blue
          ["#10e5c0", "#10e5c0"], # 5  cyan
          ["#988eca", "#988eca"], # 6  purple
          ["#fcb2e3", "#fcb2e3"], # 7  pink
          ["#51d790", "#51d790"], # 8  green
          ["#ee6388", "#ee6388"], # 9  red
          ["#fffb8d", "#fffb8d"], # 10 yellow
          ["#d1ac00", "#d1ac00"]] # 11 orange

widget_defaults = dict(
    font='Iosevka Bold',
    fontsize=14,
    padding=3,
    background=colors[3],
    opacity=0.85,
    margin=3,
)
extension_defaults = widget_defaults.copy()

### WIDGETS ###
groupbox =      widget.GroupBox(
                borderwidth = 5,
                active = colors[1],
                inactive = colors[1],
                rounded = False,
                padding_y = 5,
                padding_x = 3,
                this_current_screen_border = colors[6],
                this_screen_border = colors[1],
                other_current_screen_border = colors[6],
                other_screen_border = colors[1], 
                margin_y = 3,
                margin_x = 0,
                highlight_color = colors[3],
                highlight_method = "line",
                foreground = colors[1],
                background = colors[3],
                )
windowname =    widget.WindowName(
                max_chars=60,
                foreground=colors[1]
                )
cputext =       widget.TextBox(
                text='CPU',
                background=colors[11],
                foreground=colors[0],
                )
cpu =           widget.CPU(
                format='{load_percent}%',
                background=colors[6],
                foreground=colors[1],
                )
spacer =        widget.Spacer(
                length=10
                )
calendartext =  widget.TextBox(
                text='DATE',
                background=colors[8],
                foreground=colors[0],
                )
calendar =      widget.Clock(
                format='%A, %B %d',
                background=colors[6],
                foreground=colors[1],
                )
clocktext =     widget.TextBox(
                text='TIME',
                background=colors[5],
                foreground=colors[0],
                )
clock =         widget.Clock(
                format='%H:%M',
                background=colors[6],
                foreground=colors[1],
                )
layouttext =    widget.CurrentLayoutIcon(
                scale=0.8,
                background=colors[9],
                foreground=colors[0],
                )
currentlayout = widget.CurrentLayout(
                background=colors[6],
                foreground=colors[1],
                )
ramtext =       widget.TextBox(
                text='RAM',
                background=colors[7],
                foreground=colors[0],
                )
ram =           widget.Memory(
                format='{MemUsed: .0f}{mm}',
                background=colors[6],
                foreground=colors[1],
                )
volumetext =    widget.TextBox(
                text='VOL',
                background=colors[10],
                foreground=colors[0],
                )
volume =        widget.PulseVolume(
                volume_app='pavucontrol',
                background=colors[6],
                foreground=colors[1],
                )
networktext =   widget.TextBox(
                text='NET',
                background=colors[4],
                foreground=colors[0],
                )
network =       widget.Net(
                format='{down}',
                background=colors[6],
                foreground=colors[1],
                )
### SCREENS ###
screens = [
        Screen(top=bar.Bar([groupbox, widget.Spacer(), windowname, widget.Spacer(), cputext, cpu, spacer, ramtext, ram, spacer, networktext, network, spacer, volumetext, volume, 
        spacer, calendartext, calendar, spacer, clocktext, clock, spacer, layouttext, currentlayout],24,)),
        Screen(top=bar.Bar([groupbox, widget.Spacer(), calendartext, calendar, spacer, clocktext, clock, spacer, layouttext, currentlayout],24,)),
        Screen(top=bar.Bar([groupbox, widget.Spacer(), calendartext, calendar, spacer, clocktext, clock, spacer, layouttext, currentlayout],24,))
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
follow_mouse_focus = False
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
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
