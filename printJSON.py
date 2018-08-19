import json

filename = "JSONData.json"

with open(filename, "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

for el in data:
    print(el.get("Name"))
    for season in (el.get("Season")):
        print(season)
        for data in el.get("Season").get(season):
            print("     Episode",data.get("episodeId"))
