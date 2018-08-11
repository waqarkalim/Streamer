import time
import webbrowser
import json
import fileinput
import os
import tempfile
import sys
from pprint import pprint
from StringSuggestion import *

with open('JSONData.json') as f:
    data = json.load(f)

#inputWord = "Doctor Who"

inputWord = process(str(sys.argv[1]))

for show in data:
    if show["Name"].lower() == inputWord.lower():
        shows = show
        break

name = (shows["Name"])
seasonDict = (shows["Season"])

episodeArray = seasonDict["Season " + str(sys.argv[2])]

url = ""
#print(episodeArray)
for episodes in episodeArray:
#    print(episodes["episodeLink"])
    if (episodes["episodeId"] == str(sys.argv[3])):
        if (len(episodes["episodeLink"]) == 0):
            print("No working links, sorry...")
            sys.exit()
        url = episodes["episodeLink"][0]

if (url == ""):
    print("No working links, sorry...")
else:
    tmp=tempfile.NamedTemporaryFile(delete=False)
    path=tmp.name+'.html'

    f=open(path, 'w')
    f.write("<html lang=\"en\"><head><title>Document</title></head><body width=\"100%\" height=\"100%\"><iframe id='showVideo' src='" + url + "' width=\"100%\" height=\"100%\"></iframe></body></html>")
    f.close()
    webbrowser.open('file://' + path)
