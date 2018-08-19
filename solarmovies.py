from itertools import product
from multiprocessing import Process
from multiprocessing.dummy import Pool
import multiprocessing
import time
import re
import urllib
import requests
import json
import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path
from season import *
from episode import *
from check_link import *
from StringSuggestion import *

url = "https://solarmoviez.ru/"

inputWord = process("13 reasons WHy")
print(inputWord)

inputWord = inputWord.replace(" ", "+")

res = requests.get(url + "search/" + inputWord + ".html")

soup = BeautifulSoup(res.text, 'lxml')

#print(soup)

inputWord = inputWord.replace("+", " ")

filename = "JSONData.json"

def main():
    seasonObjList = getSeasonList()

    for seasonObj in seasonObjList:
        print(seasonObjList.index(seasonObj))
        getEpisode(seasonObj)


def getSeasonList():
    seasonList = list()

    divList = soup.find_all("div", {"class": "ml-item"})

    for div in divList:
        atag = div.find("a")
        h2tag = atag.find("h2").text
        href = atag.get("href")[:-5] + "/watching.html"

        seasonId = h2tag.split(" ")[-1]
        if (h2tag.startswith(inputWord + " - Season")):
            print(h2tag + " ::: " + href)
            seasonObj = season(seasonId, href, None)
            seasonList.append(seasonObj)


    #easonList.sort(key=lambda x: int(x.id), reverse=False)

    return seasonList

def getEpisode(season):

    episodeList = list()

    res = requests.get(season.getsiteURL())

    soup = BeautifulSoup(res.text, 'lxml')

    print(soup.find_all("iframe", {"id": "iframe-embed"}))


main()
