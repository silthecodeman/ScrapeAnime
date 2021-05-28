from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from dataScrapeFunctions import downloadEpisode, cleanShowUrls, getEpisodesDF
from bs4 import BeautifulSoup
import requests
import pandas
import time
import os
import re

if __name__ == "__main__":
	driverPath = '/{}/{}/Documents/geckodrivermac/chromedriver'.format([i for i in os.getcwd()[1:].split('/')][0], [i for i in os.getcwd()[1:].split('/')][1])

	Done = True 

	listOfUrls = [input("Anime URL >> ")]

	while Done:
		more = input("Are there any more show urls? [Y/n] ")

		if more == 'Y' or more == 'y':
			listOfUrls.append(input("Anime URL >> "))
		elif more == 'N' or more == 'n':
			Done = False
		else:
			print('Invalid Input')

		time.sleep(1)

	df = cleanShowUrls(listOfUrls)
	
	df = getEpisodesDF(df)

	for index, row in df.iterrows():
		animeName = '"{}"'.format(row['Title'].replace('/',' ').replace('.', ''))
		print(animeName)
		os.system("mkdir Animes/{}".format(animeName))
		lst = str(row['Episodes']).replace('[','').replace(']', '').replace("'", "").split(', ')[::-1]
		
		for i in range(len(lst)):
			downloadEpisode(lst[i], driverPath, 'Animes/{}/Episode{}.mp4'.format(animeName, (i+1)))
