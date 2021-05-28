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
import requests
import pandas
import time
import os
import re

def get_mp4_file_adress(driver_path, url):
	
	#initiate driver and fetch JustDubs website
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(executable_path=r'{}'.format(driver_path), options=options)
	driver.get(url)
	time.sleep(10)

	iframe = driver.find_elements_by_tag_name('iframe')[0]
	driver.switch_to.frame(iframe)

	html = driver.page_source
	driver.quit()

	soup = BeautifulSoup(html, 'html.parser')
	videoTag = soup.find_all('video', {'id':'player_html5_api'})[0]
	videoUrl = [i for i in str(videoTag).split(' ') if i[:3] == 'src'][0][4:].replace('&amp;',"&")
	
	return videoUrl

def downloadEpisode(URL, driver_path, download_path):
	mp4_file_adress = get_mp4_file_adress(driver_path, URL)

	os.system("wget --no-check-certificate -O {} {}".format(download_path, mp4_file_adress))

def getEpisodesDF(df):
	setup = {
			'Title':[],
	 		'URL':[],
	        'Episodes':[],
	        'Number of Episodes':[]
	       }

	df2 = pandas.DataFrame(setup)

	for index, row in df.iterrows():
		html = requests.get(row['URL'])
		soup = BeautifulSoup(html.text, 'html.parser')

		lst = soup.find_all('ul', {'class':'list-inline'})[0].find_all('a', href=True)

		listOfURLs = list(dict.fromkeys([i.get('href') for i in lst]))

		dic = {'Title':row['Title'], 'URL':row['URL'], 'Episodes':listOfURLs, 'Number of Episodes':row['Number of Episodes']}

		df2 = df2.append(dic, ignore_index = True)

	return df2


def cleanShowUrls(listOfUrls):
	setup = {
			'Title':[],
	 		'URL':[],
	        'Number of Episodes':[],
	        'Status':[]
	       }
	
	df = pandas.DataFrame(setup)
	failed = []
	for i in listOfUrls:
		html = requests.get(i)
		soup = BeautifulSoup(html.text, 'html.parser')

		try: 
			list_of_info = soup.find_all("div", {"id": "container-body"})[1].find_all('p')
		except:
			failed.append(i)
			continue
		try:
			title = re.sub(r"^\s+", "", str("".join([i.text for i in list_of_info if i.text[:5] == 'Title'][0].split(':')[1:])).strip(','))
		except:
			failed.append(i)
			continue
		
		url = str(i)

		try:
			numOfEpisodes = re.sub(r"^\s+", "", str("".join([i.text for i in list_of_info if i.text[:5] == 'Total'][0].split(':')[1:])).strip(','))
		except:
			failed.append(i)
			continue

		try:
			status = re.sub(r"^\s+", "", str("".join([i.text for i in list_of_info if i.text[:6] == 'Status'][0].split(':')[1:])).strip(','))
		except:
			failed.append(i)
			continue

		df2 = {'Title':title, 'URL':url, 'Number of Episodes':numOfEpisodes, 'Status': status}
		df = df.append(df2, ignore_index = True)

		#possibly use of failed list in future versions
		
	return df
