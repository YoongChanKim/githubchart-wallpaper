#!/bin/bash
screen_width="1920" #<--set here your screen's width dimension
screen_heigth="1080" #<--set here your screen's height dimension
username="FuZer" #<--set here your github username
phrases="Have a nice day $username." #<--set here your phrases

interval="60" #<--set here the seconds you want to sleep till the next update

gsettings set org.gnome.desktop.background picture-uri file://$HOME/.wallpaper.png

while true; do
	python3 ./generate.py $screen_width $screen_heigth $username "$phrases"
	gnome-web-photo --timeout=30 --mode=photo --width=$screen_width --file "web/wallpaper.html" --user-css="web/style.css"  $HOME/.wallpaper.png
   sleep $interval
done
