import json
from check_link import *

filename = "JSONData.json"

finalepisodeList = list()


with open(filename, "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

    for el in data:
        indexList = list()
        for seasons in el:
            episodeListForChecking = list()
            if (seasons == "Season"):
                seasonDict = (el.get(seasons))
                seasonDictKeys = seasonDict.keys()
                print("------------------------------------------------------------------------------------------\n\n")
                print(el.get("Name"))
                for key in seasonDictKeys:
                    episodesList = (seasonDict.get(key))
                    finalepisodeList = list()
                    #finalepisodeList = episodesList
                    for episodes in episodesList:
                        print(episodes)
                        link = episodes.get("episodeLink")
                        print(episodes.get("episodeId") + " ::: ", end='')
                        print(link)
                        if (len(link) != 0):
                            finalepisodeList.append(episodes)
                            #for links in link:
                            #    checkObj = check_link(links)
                            #    if (checkObj.check(links) == True):
                            #        finalepisodeList.append(episodes)
                            #    else:
                            #        link.remove(links)
                        if (len(link) == 0):
                            indexList.append(episodesList.index(episodes))
                            #finalepisodeList.remove(episodes)
                            #print(episodes.get("episodeId") + " Removed")
                    for episodes in episodesList:
                        link = episodes.get("episodeLink")
                        for singleLink in link:
                            print("    " + singleLink)
                    print(finalepisodeList)
                    episodeListForChecking = finalepisodeList
                #seasonDict["Season"] = episodeListForChecking
                #el["Season"] = sorted(seasonDict.keys())
                if (len(episodeListForChecking) == 0):
                    del seasonDict[key]
    for shows in data:
        if (len(shows.get("Season")) == 0):
            data.remove(shows)

with open(filename, "w", encoding='utf-8') as write_file:
    json.dump(data, write_file)
