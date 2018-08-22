import json
import collections

filename = "JSONData.json"

def bubbleSort(data, key):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i].get(key)>data[i+1].get(key):
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp


def sortNames(data):

    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i].get("Name")>data[i+1].get("Name"):
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp


def sortSeasons(data):

    for el in data:
        for seasons in el:
            #print(seasons)
            if (seasons == "Season"):
                print(el.get(seasons))
            #print(data.get(el[1]))
            #print(season)

    # for el in data:
    #     for passnum in range(len(el)-1,0,-1):
    #         for i in range(passnum):
    #             if data[i].get(key)>data[i+1].get(key):
    #                 temp = data[i]
    #                 data[i] = data[i+1]
    #                 data[i+1] = temp


def sortEpisodes(data):
    bubbleSort(data, "episodeId")

def main():
    with open(filename, "r", encoding ='utf-8') as read_file:
        data = json.load(read_file)

    #for el in data:
    #    for season in (el.get("Season")):
    #print(el.get("Season").get(season))
    #for data in el.get("Season").get(season):
    #    print(data.get("episodeId"))
    #        bubbleSort(el.get("Season").get(season), "episodeId")

    sortNames(data)
#    sortSeasons(data)


    with open(filename, "w", encoding='utf-8') as write_file:
        json.dump(data, write_file)

main()
