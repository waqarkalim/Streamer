import time
import re
import urllib
import requests
import json
import os
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
from season import *
from episode import *
from check_link import *

url = "https://www2.series9.io/movie/search/"

#inputWord = sys.argv[1]
inputWord = "The Flash"

searchUrl = url + (inputWord.lower()).replace(" ", "-")
print(searchUrl)

driver = webdriver.PhantomJS()
driver.get(searchUrl)

time.sleep(10)

res = requests.get(searchUrl)
soup = BeautifulSoup(driver.page_source, 'lxml')
filename = "JSONData.json"

def main():
    seasonList = getSeasonList()

    getEpisodeList(seasonList)

def getSeasonList():
    seasonList = list()

    movieList = soup.find_all('div', {"class": "ml-item"})

    for movie in movieList:
        atag = movie.find('a')
        title = str(atag.get("oldtitle"))
        link = str(atag.get("href"))

        titleSplit = title.split(" ")
        seasonId = titleSplit[-1]
        if ((title.startswith(inputWord + " - ")) and (titleSplit[-2] == "Season")):
            #print(title, link)
            seasonObj = season(seasonId, link, None)
            seasonList.append(seasonObj)
    seasonList.sort(key=lambda x: x.id)

    return seasonList

def getEpisodeList(seasonList):

    for season in seasonList:

        episodeList = list()
        res = requests.get(season.getsiteURL() + "/watching.html")

        soup = BeautifulSoup(res.text, 'lxml')

        NumberOfEpisodes = (soup.find("input", {"name": "episode_report"})).get("value")
        print(NumberOfEpisodes)

        for i in range(1, int(NumberOfEpisodes)+1):
            newURL = season.getsiteURL() + "/watching.html?ep=" + str(i)

            driver.get(newURL)
            time.sleep(5)

            res = requests.get(newURL)
            soup = BeautifulSoup(driver.page_source, 'lxml')

            #print(soup)
            epList = soup.find_all("video", {"class":"jw-video jw-reset"})
            print(epList)
            #sourceLink = epList.get_attribute("src")
            #print(sourceLink)

#        epList = soup.find("video", {"class":"jw-video jw-reset"})
#        print(epAtags)

        print("Season " + season.getId() + " - " + season.getsiteURL())

#    movieList = driver.find_element_by_xpath("//*[@id='cls_search']/div[2]/div[1]")
#    print(movieList.get_attribute("href"))
#    for movie in movieList:
#        print(movie.get_attribute("oldtitle"))
#        title = movie.text
#        titleSplit = title.split(" ")
#        titleSplit[0] = (titleSplit[0].split("\n"))[-1]
#        title = ' '.join(titleSplit)
#        link = movie.get_attribute("href")
#        if ((title.startswith(inputWord + " - ")) and (titleSplit[-2] == "Season")):
#            print(title)
#            print(link)

main()
