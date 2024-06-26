#!/bin/sh

##
## Run inside the flatpak build and move all files to their locations.
##

set -e
cd "`dirname \"$0\"`"

ID=io.github.niccokunzmann.python_dhcp_server
# persistent config directory
config=/var/config

echo -------------------------------------------------
echo Build Context for DEBUG
echo pwd=`pwd`
ls -la
dirname `pwd`
ls -la `pwd`/..
echo -------------------------------------------------


echo Install the executable

mkdir -p /app/bin/
install -D python_dhcp_server /app/bin/python_dhcp_server
mv ../server /app/

echo Install metadata
## see https://docs.flatpak.org/en/latest/conventions.html#metainfo-files
## see https://docs.flathub.org/docs/for-app-authors/metainfo-guidelines/#path-and-filename

mkdir -p files/share/app-info
cp $ID.xml files/share/app-info/
mkdir -p /app/share/metainfo/
mv $ID.xml /app/share/metainfo/$ID.metainfo.xml


echo Install Desktop file
## see https://docs.flatpak.org/en/latest/conventions.html#desktop-files

mkdir -p /app/share/applications/
cp $ID.desktop /app/share/applications/


echo Install icons
## see https://docs.flatpak.org/en/latest/conventions.html#application-icons

mkdir -p /app/share/icons/hicolor/scalable/apps/
mv ../images/icon.svg /app/share/icons/hicolor/scalable/apps/$ID.svg

echo Setup Persistent Storage
mkdir -p "$config"
mv /app/server/dhcpgui.conf /app/server/dhcpgui.conf.bak
ln -sT "$config/dhcpgui.conf" /app/server/dhcpgui.conf

echo -------------------------------------------------
echo Build Context for DEBUG
echo
echo pwd=`pwd`
ls -la
echo
dirname `pwd`
ls -la `pwd`/..
echo
echo "$config"
ls -la "$config"
echo -------------------------------------------------


echo Install done
