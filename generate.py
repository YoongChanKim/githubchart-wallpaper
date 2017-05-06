#! /usr/bin/python3

import time
import subprocess

html = """
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300" rel="stylesheet">
</head>

<body>
    <div class="clock">
        <h1>%s</h1>
        <h2>%s</h2>
    </div>
    <div class="git">
        <img src="http://ghchart.rshah.org/%s">
    </div>
</html>
"""

css = """
body {
    background-image: url(wallpaper);
    background-repeat: no-repeat;
    background-size: %spx %spx;
    width: %spx;
    height: %spx;
    overflow: hidden;
}

.clock {
    position: absolute;
    text-align: center;
    left: 0;
    top: 35%%;
    width: 100%%;
    text-align: center;
}

.clock h1 {
    color: rgba(255, 255, 255, 1.0);
    font-size: 150px;
    margin: 0px;
    font-family: 'Open Sans', sans-serif
}

.clock h2 {
    color: rgba(255, 255, 255, 0.7);
    font-size: 50px;
    margin: 0px;
    font-family: 'Open Sans', sans-serif
}

.git {
    position: absolute;
    text-align: center;
    top: 73%%;
    left: 0%%;
    width: 100%%;
}

img {
    background-color: rgba(250, 250, 250, 0.2);
    padding: 20px;
    border-radius: 10px;
}

"""

width = "1920"
height = "1080"
user = "FuZer"
phrases = "Have a nice day, " + user + "."

pred = 0

subprocess.run("gsettings set org.gnome.desktop.background picture-uri file://$HOME/.wallpaper.png", shell=True)

while True:
    if(time.strftime("%M") == pred):
        time.sleep(1)
        continue

    time_format = "{}:{}".format(time.strftime("%H"), time.strftime("%M"))

    with open('web/wallpaper.html', 'w') as html_file:
        html_file.write(html % (time_format, phrases, user))

    with open('web/style.css', 'w') as css_file:
        css_file.write(css % (width, height, str(int(width)-10), height))

    subprocess.run('gnome-web-photo --timeout=30 --mode=photo --width={} --file "web/wallpaper.html" --user-css="web/style.css"  $HOME/.wallpaper.png'.format(width), shell=True)
    pred = time.strftime("%M")

