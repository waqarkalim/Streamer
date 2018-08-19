import json
import sys
from StringSuggestion import *

filename = "JSONData.json"

#inputWord = "Doctor Who"

#inputWord = process(sys.argv[1])

def removeFromJSON():
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonInput = json.load(f)
        for shows in jsonInput:
            if (shows.get("Name").lower()  == inputWord.lower()):
                jsonInput.remove(shows)

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(jsonInput, f)

def removeEmptyShows():
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonInput = json.load(f)
        for shows in jsonInput:
            if (len(shows.get("Season"))  == 0):
                jsonInput.remove(shows)

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(jsonInput, f)

#removeFromJSON()
removeEmptyShows()
