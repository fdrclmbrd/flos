# flOS - A collection of software to turn Hyprland window manager into a fully functional desktop environment

## What's flos?

Hyprland is one of the gratest Wayland compositor and window manager aviable today which main strenght sits in the few number of softwares bundled with its installation. It is, hence, up to the end-user to install all the necessary software in order "to make Wayland / Hyprland / other apps work correctly", quoting Hyprland's wiki.

The flOS project, similarly to DTOS by [Derek Taylor](https://gitlab.com/dwt1/distro.tube/-/tree/master/dtos "DTOS repo on GitLab"), has the aim to provide an installer to a boundle of softwares and script which can provide a functional desktop experience with the least number of packages following a specific personal philosophy.
The choices taken are based on the following:

1. Less is more
2. Keyboard-centric experience
3. Maximum use of screen pixels

In particular, from point 3. it follows the main *non*-feature which is the **absence of a panel always present on screen**.
Currently, the flos installation script works on Arch Linux based systems and it has been tested on pure Arch Linux.

### Window Managment

Since there is no panel always on screen, it is necessary to have a way to reach any window on any virtual desktop quickly: this is done via ``hyprland-window-switcher.py`` a simple Python script which generate a temporary desktop file in ``~/.local/share/applications/`` floder for every opened window, Rofi to parse them and ``hyprctl`` to move focus to the desired window; by default, this script is binded to ``SUPER`` + ``Tab`` key combination.
