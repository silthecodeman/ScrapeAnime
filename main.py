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
import orginizeShows
import getShows
import requests
import pandas
import time
import os
import re

if __name__ == "__main__":
	pathelem = [i for i in os.getcwd()[1:].split('/')]

	shows = getShows.showsFinder('/{}/{}/Documents/geckodrivermac/chromedriver'.format(pathelem[0], pathelem[1]), 1)
	result = shows.run('completed')

	df = orginizeShows.cleanShowUrls(result)
	
	print(df)
