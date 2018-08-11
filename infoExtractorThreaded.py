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

url = "https://www7.fmovies.io/search.html?keyword="

#inputWord = "The Vampire Diaries"

inputWord = process(sys.argv[1])
print(inputWord)
inputWord = inputWord.replace(" ", "+")

res = requests.get(url + inputWord)

inputWord = inputWord.replace("+", " ")

soup = BeautifulSoup(res.text, 'lxml')
filename = "JSONData.json"




def checkIfFileEmpty(filename):
    filePath = Path(filename)
    if filePath.is_file():
        if ((os.stat(filename).st_size) == 0):
            print(filename + " is empty.")
            return True
    print(filename + " is NOT empty.")
    return False

def jsonInitializeList(filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump([], f)
        print("JSON list initialized...")

def checkIfShowInJSON(filename, inputWord):
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonInput = json.load(f)
        for shows in jsonInput:
            if (shows.get("Name").lower() == inputWord.lower()):
                return True
        return False

def jsonWrite(seasonList, inputWord):

    showList = list()

    showdict = dict()
    showdict["Name"] = inputWord
    seasondict = dict()
    for season in seasonList:
        episodeList = list()
        for episode in season.getEpisodeList():
            episodedict = dict()
            episodedict["episodeId"] = episode.getId()
            episodedict["episodeLink"] = episode.getsourceLink()
            episodedict["episodeName"] = episode.getName()
            episodedict["episodeSiteURL"] = episode.getsiteURL()
            episodeList.append(episodedict)

        seasondict["Season " + str(season.getId())] = episodeList
    showdict["Season"] = seasondict
#    showList.append(showdict)

    with open(filename, mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)

    with open(filename, mode='w', encoding='utf-8') as feedsjson:
        entry = showdict
        feeds.append(entry)
        json.dump(feeds, feedsjson)
        print("JSON data written to 'JSONData.json'...")

def getSourceLinks(seasonList):

    AtLeastOneAlive = False
    for season in seasonList:
        print("Season " + str(season.getId()))
        for episode in season.getEpisodeList():
            res = requests.get(episode.getsiteURL())
            soup = BeautifulSoup(res.text, 'lxml')

            scriptTags = soup.find_all("script")
            print("     Episode " + str(episode.getId()))
            for script in scriptTags:
                if ("link_server_f" in str(script)):
                    sourceLinkList = re.findall('"https:/([^"]*)"', str(script))
                    for sourceLink in sourceLinkList:
                        sourceLinkList[sourceLinkList.index(sourceLink)] = "https:/" + sourceLink
                    for sourceLink in sourceLinkList:
                        checkObj = check_link(sourceLink)
                        #checkObj.check(sourceLink)
                        if (checkObj.check(sourceLink) == False):
                            #if (is_fully_alive(sourceLink) == False):
                            del sourceLinkList[sourceLinkList.index(sourceLink)]
                        else:
                            AtLeastOneAlive = True
                    #insert broken link checking
            if (AtLeastOneAlive == False):
                print("         sorry, no working links found...")
            episode.setsourceLink(sourceLinkList)

def getSourceLinkforOneSeason(season):
    AtLeastOneAlive = False
    for episode in season.getEpisodeList():
        res = requests.get(episode.getsiteURL())
        soup = BeautifulSoup(res.text, 'lxml')

        scriptTags = soup.find_all("script")
        print("     Episode " + str(episode.getId()))
        for script in scriptTags:
            if ("link_server_f" in str(script)):
                sourceLinkList = re.findall('"https:/([^"]*)"', str(script))
                for sourceLink in sourceLinkList:
                    sourceLinkList[sourceLinkList.index(sourceLink)] = "https:/" + sourceLink
                for sourceLink in sourceLinkList:
                    checkObj = check_link(sourceLink)
                    #checkObj.check(sourceLink)
                    if (checkObj.check(sourceLink) == False):
                        #if (is_fully_alive(sourceLink) == False):
                        del sourceLinkList[sourceLinkList.index(sourceLink)]
                    else:
                        AtLeastOneAlive = True
                #insert broken link checking
        if (AtLeastOneAlive == False):
            print("         sorry, no working links found...")
        episode.setsourceLink(sourceLinkList)

def is_fully_alive(url, live_check = False):
    try:
        if not urllib2.urlparse.urlparse(url).netloc:
            return False

        website = urllib2.urlopen(url)
        html = website.read()

        if website.code != 200 :
            return False

        # Get all the links
        for link in re.findall('"((http|ftp)s?://.*?)"', html):
            url = link[0]

            if not urllib2.urlparse.urlparse(url).netloc:
                return False

            if live_check:
                website = urllib2.urlopen(url)

                if website.code != 200:
                    print ("Failed link : ", url)
                    return False

    except (Exception):
        #print ("Errored while attempting to validate link : ", url)
        return False

    return True


def getSeasonList():
    seasonList = list()
    article = soup.find('article')
    for el in article.find_all('a'):
        title = str(el.get('title'))
        link = str(el.get('href'))
        if (title.endswith(" Movie")) and (link).startswith("/watch/") and (((title.lower()).startswith(inputWord.lower() + " - ")) or ((title.lower().startswith(inputWord.lower() + ": ")))):
            link = "https://www7.fmovies.io" + link
            print(title + " ::: " + link)

            titlesplit = title.split(" ")

            if ("Season" in titlesplit):
                seasonId = titlesplit[titlesplit.index("Season") + 1]
                #print(seasonId)

            seasonObj = season(seasonId, link, None)
            seasonList.append(seasonObj)

    seasonList.sort(key=lambda x: x.id, reverse=True)

    return seasonList


def getEpisode(season):

    episodesList = list()
    res = requests.get(season.getsiteURL())
    soup = BeautifulSoup(res.text, 'lxml')
    scripts = soup.find_all("script")

    episodesiteURLs = soup.find_all("div", {"class": "server"})


    #print(episodesiteURLs)

    #print(episodesiteURLs[-1])

    atags = episodesiteURLs[-1].findAll('a')
    #print(atags)
    for atag in atags:
        atext = atag.find("span").text
#            atext = atag.text.strip("\n")
#            atextsplit = atext.split(" ")
#            atextsplit.pop()
#            atext = " ".join(atextsplit)
        atext = atext.split(" ")
#            print(atext)
        #print(atext)
        if "Episode" in atext:
            indexOfEpisode = atext.index("Episode")
            if (len(atext) == (indexOfEpisode + 1)):
                continue
            if (atext[indexOfEpisode + 1] == "Special:"):
                continue
            else:
                episodeId = atext[atext.index("Episode") + 1]
            if str(episodeId).endswith(":"):
                episodeId = episodeId[:-1]
            if (len(str(episodeId)) == 2) and (str(episodeId)[0] == "0"):
                episodeId = episodeId[1:]
            if (":" in episodeId):
                episodeId = episodeId.split(":")[0]
            atext = " ".join(atext)
        else:
            for el in atext:
                if ((el.lower()[0] == "e") and (len(el) == 7)):
                    indexOfEpisode = atext.index(el)
                    messedUpEpisodeString = el
                    break
            if (len(atext) == (indexOfEpisode + 1)):
                continue
            if (atext[indexOfEpisode + 1] == "Special:"):
                continue
            else:
                episodeId = atext[atext.index(messedUpEpisodeString) + 1]
            if str(episodeId).endswith(":"):
                episodeId = episodeId[:-1]
            if (len(str(episodeId)) == 2) and (str(episodeId)[0] == "0"):
                episodeId = episodeId[1:]
            if (":" in episodeId):
                episodeId = episodeId.split(":")[0]
            atext = " ".join(atext)
        ahref = str(atag.get('href'))
        episodeId = re.sub("[^0-9]", "", episodeId)
            #print(atext + " ............... " + ahref)
        episodeObj = episode(episodeId, atext,"https://www7.fmovies.io" + ahref, None)
        episodesList.append(episodeObj)
        season.setEpisodeList(episodesList)

def getEpisodeList(seasonList):

    for season in seasonList:

        episodesList = list()
        res = requests.get(season.getsiteURL())
        soup = BeautifulSoup(res.text, 'lxml')
        scripts = soup.find_all("script")

        episodesiteURLs = soup.find_all("div", {"class": "server"})


        #print(episodesiteURLs)

        #print(episodesiteURLs[-1])

        atags = episodesiteURLs[-1].findAll('a')
        #print(atags)
        for atag in atags:
            atext = atag.find("span").text
#            atext = atag.text.strip("\n")
#            atextsplit = atext.split(" ")
#            atextsplit.pop()
#            atext = " ".join(atextsplit)
            atext = atext.split(" ")
#            print(atext)
            indexOfEpisode = atext.index("Episode")
            if (len(atext) == (indexOfEpisode + 1)):
                continue
            if (atext[indexOfEpisode + 1] == "Special:"):
                continue
            else:
                episodeId = atext[atext.index("Episode") + 1]
            if str(episodeId).endswith(":"):
                episodeId = episodeId[:-1]
            if (len(str(episodeId)) == 2) and (str(episodeId)[0] == "0"):
                episodeId = episodeId[1:]
            if (":" in episodeId):
                episodeId = episodeId.split(":")[0]
            atext = " ".join(atext)
            ahref = str(atag.get('href'))
            #print(atext + " ............... " + ahref)
            episodeObj = episode(episodeId, atext,"https://www7.fmovies.io" + ahref, None)
            episodesList.append(episodeObj)
        season.setEpisodeList(episodesList)
#        for episode in episodesiteURLs:
#            episodeTitle = str(episode.get('title'))
#            episodeLink = str(episode.get('href'))

#            print(episode)
#print(episodeTitle + " ... " + episodeLink)

def calculateParallel(seasons, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(getEpisode, seasonList)
    pool.close()
    pool.join()
    return results



if __name__ == '__main__':

    start_time = time.time()

    if checkIfFileEmpty(filename):
        jsonInitializeList(filename)

    if (checkIfShowInJSON(filename, inputWord)):
        print("Show already in JSON File...")
    else:
        seasonList = getSeasonList()
        print(seasonList)

    #    with multiprocessing.Pool(processes=8) as pool:
    #        pool.starmap(getEpisode, product(seasonList))

        pool = Pool(8)

        pool.map(getEpisode, seasonList)

        #with multiprocessing.Pool(processes=8) as pool:
        #    pool.starmap(getSourceLinkforOneSeason, product(seasonList))

    #    results = calculateParallel(seasonList, 4)
#        p = Process(target=getEpisode, args=('season',))
#        getEpisode(season)
#        getEpisodeList(seasonList)

#        pool = Pool(4)

 #       pool.map(getSourceLinkforOneSeason, seasonList)

        getSourceLinks(seasonList)

        jsonWrite(seasonList, inputWord)

    print("--- %s seconds ---" % (time.time() - start_time))
