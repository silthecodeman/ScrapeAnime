from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import getShows
import time
import os

if __name__ == "__main__":
	pathelem = [i for i in os.getcwd()[1:].split('/')]
	shows = getShows.showsFinder('/{}/{}/Documents/geckodrivermac/chromedriver'.format(pathelem[0], pathelem[1]), 64)
	result = shows.run('completed')
	print(result)
