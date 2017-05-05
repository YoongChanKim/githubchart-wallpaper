#! /usr/bin/python3

import sys
import time

html = """
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="style.css">
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
    font-family: sans-serif;
}

.clock h2 {
    color: rgba(255, 255, 255, 0.7);
    font-size: 50px;
    margin: 0px;
    font-family: sans-serif;
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

width = sys.argv[1]
height = sys.argv[2]
user = sys.argv[3]
phrases = sys.argv[4]

time_format = "{}:{}".format(time.strftime("%H"), time.strftime("%M"))

with open('web/wallpaper.html', 'w') as html_file:
    html_file.write(html % (time_format, phrases, user))

with open('web/style.css', 'w') as css_file:
    css_file.write(css % (width, height, str(int(width)-10), height))

