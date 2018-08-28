from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup
import re, os, lxml.etree, json, requests, time

#chrome_options = Options()

#chrome_options.add_argument('-headless')
#chrome_options.add_argument('--windows-size=1920x1080')
#chrome_options.Proxy = None

#print(os.getcwd() + "/chromedriver")

#chrome_driver = os.getcwd() + "/chromedriver"

#os.environ["webdriver.chrome.driver"] = chrome_driver

#browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

url = "https://123movie.cc/seasons/flash-season-4/"

#browser.get(url)

options = Options()
options.add_argument("--headless")
options.add_argument("--mute-audio")
driver = webdriver.Firefox(firefox_options=options)

res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

episodeList = soup.find_all("li", {"class": "mark"})

for episode in episodeList:
    print("--------------------")
    print(episode.find("div", {"class": "numerando"}).find("button"))

driver.get(url)
selectedButton = driver.find_element_by_class_name("liopv")
print(selectedButton.text)


divList = soup.find_all("div")

for div in divList:
    print(div)

#browser.get(url)
print(len(episodeList))
#print(driver.page_source)

selectedButton.click()
time.sleep(5)

playButton = driver.find_element_by_class_name("vjs-big-play-button")
playButton.click()

#time.sleep(5)

#print(driver.page_source)

#element = driver.find_element_by_id("videojs_html5_api")
#print(element)

try:
    driver.close()
except NoAlertPresentException:
    print("Error while closing")



quit()
