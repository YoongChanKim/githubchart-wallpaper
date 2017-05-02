#! /usr/bin/python3

import sys

html = """
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>%s</h1>
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

h1 {
    color: rgba(255, 255, 255, 0.8);
    font-size: 80px;
    font-family:sans-serif;

    position: absolute;
    text-align: center;
    left: 0;
    top: 30%%;
    width: 100%%;
    text-align: center;
}

.git {
    position: absolute;
    text-align: center;
    top: 50%%;
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

with open('web/wallpaper.html', 'w') as html_file:
    html_file.write(html % (phrases, user))

with open('web/style.css', 'w') as css_file:
    css_file.write(css % (width, height, str(int(width)-10), height))

print('Finish Configuration')
