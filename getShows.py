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
import time
import os

class showsFinder:

	def __init__(self, path, numberOfPages):
		self.path = path
		self.numberOfPages = numberOfPages

	def run(self, Status):
		driver = self.startBrowser()

		if Status != 'all':
			self.filter(Status, driver)

		Links = self.downloadLinks(self.numberOfPages, driver)

		self.stopBrowser(driver)

		return Links


	def startBrowser(self):
		#Make sure that chromedriver is in empty directory labled 'geckodrivermac' inside ~/Documents directory
		path = self.path

		#initiate driver and fetch JustDubs website
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
		driver = webdriver.Chrome(executable_path=r'{}'.format(path), options=options)
		driver.get('https://ww1.justdubs.tv/anime-series')
		time.sleep(1)

		return driver


	def stopBrowser(self, driver):
		driver.quit()


	def filter(self, Status, driver):
		status = Select(driver.find_element_by_id('status-selector'))
		if Status == 'completed':
			status.select_by_value('completed')
		elif Status == 'ongoing':
			status.select_by_value('ongoing')

		driver.find_elements_by_class_name('btn-primary')[0].click()


	def downloadLinks(self, number_of_pages, driver):
		# number of pages with completed anime
		pages = number_of_pages
		lst = []
		for i in range(pages):

			time.sleep(7)
			html = driver.page_source
			soup = BeautifulSoup(html, 'html.parser')

			lst = lst + soup.find("ul", {"id": "anime_grid"}).find_all('a', href=True)
			if i != pages:
				driver.find_elements_by_class_name('page-link')[-2].click()

			# Turn list to dict and back to list to remove duplicate URLs
			listOfURLs = list(dict.fromkeys([i.get('href') for i in lst]))
		
		return listOfURLs

if __name__ == "__main__":
	pathelem = [i for i in os.getcwd()[1:].split('/')]
	getShows = showsFinder('/{}/{}/Documents/geckodrivermac/chromedriver'.format(pathelem[0], pathelem[1]), 64)
	result = getShows.run('completed')
	print(result)
