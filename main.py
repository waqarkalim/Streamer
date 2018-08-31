import os
from bs4 import BeautifulSoup
import re
import urllib
import requests
import sys
import time
import multiprocessing as mp
import string
import random
from itertools import product

#infoExtractorThreaded.main()

#os.system("python3 infoExtractorThreaded.py 'The Flash'")

#url = "https://www.imdb.com/list/ls062075869/?sort=list_order asc&st_dt=&mode=simple&page=1&ref_=ttls_vw_smp"

#res = requests.get(url)

#soup = BeautifulSoup(res.text, 'lxml')

#listofNames = soup.find_all("div", {"class": "lister-item mode-simple"})

#Names = list()

start_time = time.time()

Names = ["Doctor Who", "The Vietnam War", "Game of Thrones", "American Gods", "Vikings", "Star Trek: Discovery", "Blue Planet II", "The Expanse", "Legion", "Black Mirror", "The Punisher", "Fortitude", "Emerald City", "Nova", "The Young Pope", "Will", "A Series of Unfortunate Events", "Sun Records", "The Get Down", "American Crime", "Fargo", "Top of the Lake", "Stranger Things", "Taboo", "The Magicians", "The 100", "13 Reasons Why", "Vice", "The Late Show with Stephen Colbert", "Underground", "Incorporated", "The Handmaid's Tale", "Sherlock", "Pure Genius", "Z: The Beginning of Everything", "This Is Us", "Feud", "Crashing", "Into the Badlands", "Iron Fist", "The Leftovers", "The White Princess", "Brockmire", "Dear White People", "The Last Kingdom", "I Love Dick", "The Keepers", "House of Cards", "Designated Survivor", "The Good Fight", "Better Call Saul", "Silicon Valley", "Jamestown", "Genius", "Riviera", "GLOW", "Preacher", "Cleverman", "Gypsy", "I'm Dying Up Here", "Broken", "The Defiant Ones", "Ozark", "Still Star-Crossed", "Ray Donovan", "Atypical", "Midnight, Texas", "The Deuce", "Narcos", "Skyward", "Electric Dreams", "StartUp", "American Horror Story", "Alias Grace", "One Mississippi", "Fear the Walking Dead", "South Park", "Big Little Lies", "Bad Blood", "Curb Your Enthusiasm", "Channel Zero", "Mr. Mercedes", "Mindhunter", "Gunpowder", "Bob's Burgers", "Shameless", "Kingdom", "The Marvelous Mrs. Maisel", "Godless", "Damnation", "Happy!", "The Flash", "Dexter"]

def process(name):
    #os.system('python3 infoExtractorThreaded.py "' + name + '"')
    os.system('python3 infoExtractorThreadedbk.py "' + name + '"')
    #os.system('python3 infoExtractorThreaded.py "' + name + '" > /dev/null 2>&1')
    print(name + " Completed")

#for name in Names:
#    print(str(Names.index(name) + 1) + ". " + name )
#    os.system('python3 infoExtractorThreaded.py "' + name + '" > /dev/null 2>&1 && echo "' + name + ' Completed' + '"&')
#    if ((Names.index(name) % 5) == 0):
#        os.system('wait')


#pool = mp.Pool(processes=4)

#[pool.apply(process, args=(x,)) for x in Names]

with mp.Pool(processes=4) as pool:
    pool.starmap(process, product(Names, repeat=1))

end_time = time.time()

time = end_time - start_time


day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time


os.system('python3 removeShow.py')
os.system('python3 removeShow.py')
os.system('python3 removeShow.py')
os.system('python3 sortJSON.py')

print("Final Time taken --- d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
#for el in listofNames:
#    print(el.find("a"))
#    Names.append(el.find("div", {"class": "lister-item-content"}))
    #var1 = (el.find("div", {"class": ""})).find("div")

#for el in Names:
#    print(el.find("a").text)
#print(listofNames)

