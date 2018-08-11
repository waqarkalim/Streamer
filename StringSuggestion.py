import urllib, requests, re
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q="
#inputWord = "the flahs"

def process(inputWord):

    newURL = url + inputWord.replace(" ","+") + "+tv+series+wikipedia"

    res = requests.get(newURL)
    soup = BeautifulSoup(res.text, 'lxml')

    tag = soup.find("h3", {"class":"r"})
    atag = tag.find('a').text
    if (atag.endswith(" - Wikipedia")):
        atag = atag[:-(len(" - Wikipedia"))]
    atag = re.sub(r'\([^)]*\)', '', atag)
#    print(atag)
    result = atag
    if (result[-1] == " "):
        result = result[:-1]
    #print(result + " " + str(len(result)))
    return result
