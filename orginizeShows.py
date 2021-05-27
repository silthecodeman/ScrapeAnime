from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

def cleanShowUrls(listOfUrls):
	setup = {
		'Title':[],
	 	'URL':[],
	        'Number of Episodes':[],
	        'Status':[]
	       }
	
	df = pd.DataFrame(setup)
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

if __name__ == '__main__':
	cleanShowUrls(['https://ww1.justdubs.tv/anime/64-fairy-tail-english-dub'])
