from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from pyvirtualdisplay import Display

from bs4 import BeautifulSoup
import re, os, lxml.etree, json, requests, time

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

#chrome_options = Options()

#chrome_options.add_argument('-headless')
#chrome_options.add_argument('--windows-size=1920x1080')
#chrome_options.Proxy = None

#print(os.getcwd() + "/chromedriver")

#chrome_driver = os.getcwd() + "/chromedriver"

#os.environ["webdriver.chrome.driver"] = chrome_driver

#browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

#url = "https://123movie.cc/seasons/flash-season-4/"
start_time = time.time()

url = "https://www9.fmovies.io/watch/marvels-cloak-dagger-season-1-episode-10-colony-collapse.html"

#browser.get(url)

display = Display(visible=0, size=(800, 800))
display.start()

options = Options()
options.add_argument("--headless")
options.add_argument("--mute-audio")

driver = webdriver.Chrome(options=options)
#driver = webdriver.Firefox(firefox_options=options)
driver.get(url)
print("Driver got url...")
#print(driver.page_source)

oldSource = driver.page_source
#res = requests.get(url)

#soup = BeautifulSoup(res.text, 'lxml')

try:
    elementIcon = driver.find_element_by_xpath("//*[@id=\"server-f2\"]/div[2]/i")
    print("Icon found...")
    driver.execute_script("arguments[0].click();", elementIcon)
    #elementIcon.click()
    print("Icon clicked...")
    #time.sleep(5)

    playerElement = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"server-f2\"]")))

    #playerElement = driver.find_element_by_class_name("player.current")
    print(playerElement.get_attribute("innerHTML"))
    soup = BeautifulSoup(playerElement.get_attribute("innerHTML"), 'lxml')
    iframeSrc = soup.find("iframe")['src']
    print(iframeSrc)
except NoAlertPresentException:
    print("NoAlertPresentException found")
except UnexpectedAlertPresentException:
    print("UnexpectedAlertPresentException found")
#episodeList = soup.find_all("li", {"class": "mark"})

#for episode in episodeList:
#    print("--------------------")
#    print(episode.find("div", {"class": "numerando"}).find("button"))

#driver.get(url)
#selectedButton = driver.find_element_by_class_name("liopv")
#print(selectedButton.text)


#divList = soup.find_all("div")

#for div in divList:
#    print(div)

#browser.get(url)
#print(len(episodeList))
#print(driver.page_source)

#selectedButton.click()
#time.sleep(5)

#playButton = driver.find_element_by_class_name("vjs-big-play-button")
#playButton.click()

#time.sleep(5)

#print(driver.page_source)

#element = driver.find_element_by_id("videojs_html5_api")
#print(element)

try:
    driver.close()
except NoAlertPresentException:
    print("Error while closing")



quit()


end_time = time.time()

time = end_time - start_time


day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

print("Final Time taken --- d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
