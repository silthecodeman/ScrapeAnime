from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import requests
import time
import os


def filter(driver):
	status = Select(driver.find_element_by_id('status-selector'))
	status.select_by_value('completed')
	driver.find_elements_by_class_name('btn-primary')[0].click()
  
if __name__ == '__main__':
  	#Get coputer path
	pathelem = [i for i in os.getcwd()[1:].split('/')]
	#Make sure that chromedriver is in empty directory labled 'geckodrivermac' inside ~/Documents directory
	path = '/{}/{}/Documents/geckodrivermac/chromedriver'.format(pathelem[0], pathelem[1])

	#initiate driver and fetch 2048 website
	driver = webdriver.Chrome(executable_path=r'{}'.format(path))
	driver.get('https://ww1.justdubs.tv/anime-series')
	time.sleep(1)

	filter(driver)
