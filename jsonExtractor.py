import time
import webbrowser
import json
import fileinput
import os

from selenium import webdriver
from pprint import pprint

with open('testfile.json') as f:
    data = json.load(f)

shows = data[0]

name = (shows["Name"])
seasonDict = (shows["Season"])

episodeArray = seasonDict["Season 8"]

url = ""
for episodes in episodeArray:
    print(episodes["episodeLink"])
    if (episodes["episodeId"] == 3):
        url = episodes["episodeLink"]
        #webbrowser.get("/usr/bin/google-chrome").open(episodes["episodeLink"])

with open('index.html', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('$video', url)
print(filedata)


with open('index.html', 'w') as file:
    file.write(filedata)

webbrowser.open("index.html")
time.sleep(5)


with open('index.html', 'r') as file:
    filedata = file.read()

filedata = filedata.replace(url, '$video')
print(filedata)


with open('index.html', 'w') as file:
    file.write(filedata)
