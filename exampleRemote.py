from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))

display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

browser.get('http://www.google.com')
print(browser.title)
browser.quit()

display.stop()
