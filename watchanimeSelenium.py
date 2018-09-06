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

url = "http://watchanimeonline.me/boruto-naruto-next-generations-sub/"

display = Display(visible=0, size=(800, 600))
display.start()

options = Options()
options.add_argument("--headless")
options.add_argument("--mute-audio")

driver = webdriver.Chrome(options=options)
driver.get(url)

try:
    elementButtons = driver.find_elements_by_class_name("btn-eps")
    for button in elementButtons:
        print(button.text)
except NoAlertPresentException:
    print("NoAlertPresentException found...")
except UnexpectedAlertPresentException:
    print("UnexpectedAlertPresentException found...")


