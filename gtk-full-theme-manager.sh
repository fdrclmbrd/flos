#!/bin/bash

#APPLICATION_THEME="Materia-dark-compact"
#APPLICATION_THEME="Jasper-Blue-Dark-Compact"
APPLICATION_THEME="Fluent-round-Dark-compact"
ICON_THEME="Qogir-dark"
CURSOR_THEME="capitaine-cursors"
FONT="Urbanist Medium 12"

INTERFACE="org.gnome.desktop.interface"

gsettings set "$INTERFACE" gtk-theme "$APPLICATION_THEME"
gsettings set "$INTERFACE" icon-theme "$ICON_THEME"
gsettings set "$INTERFACE" cursor-theme "$CURSOR_THEME"
gsettings set "$INTERFACE" font-name "$FONT"
