# ScrapeAnime

ScrapeAnime is a Python script that allows anyone to download a whole show from the website 'ww1.JustDubs.tv'. There is little room to contrive and make imporvized scripts, however 'dataScrapeFunctions.py' contains 4 functions that could be useful.

## Installation
```bash
git clone "https://github.com/silthecodeman/ScrapeAnime.git"
cd scrapeAnime
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Prerequisites and Other Information
GNU Wget must be installed for the script to work. This program has only been tested on macOS Big Sur Version 11.3.1 and is expected to work the same on Linux. This program has only been tested with Python 3.9.5 and will most likely work with Python 3.7 and up.

## How to Use
To initially run the program, the file 'main.py' needs to be run in the terminal.
```bash
python3 main.py
```
When runing the program, the comand line will prompt the user to enter a url. 
```bash
Anime URL >> 
```
This url is specific to 'ww1.JustDubs.tv' and will only work if it is a url that leads to the home page of the intended anime. The page in question should also contin a list of the anime's episodes as well as general information. Go to https://ww1.justdubs.tv/anime/1565-akame-ga-kill-english-dub for an example of what the url should look like.

Next, the comand prompt will ask if there is any more shows you wish to download.
```bash
Are there any more show urls? [Y/n] 
```

If there is, the program will ask for another url and the process will be repeated until there are no more urls to be scraped.
The program will then run and orginize the anime and it's episodes into a folder named 'Animes'.

As a rule of thumb, don't be discuraged if the program takes a while to run as there are several variables that could be the cause for the time delay including file size or internet connection.

## Issues
There are no issues execpt for the fact that some anime are stored in different databases and thus when the program attemmpts to use the command 'wget' it fails. However during the creation of this project, there was but one instnace of this occuring and refusing to download.

# Documentation

## dataScrapeFunctions.get_mp4_file_adress(driver_path, url)
'url' refers to the url that was imputed by the user at the beginning of the program.
'driver_path' refers to the path of the Chrome driver used by Selenium.

The function returns the url of the .mp4 file. 

## dataScrapeFunctions.downloadEpisode(URL, driver_path, download_path)
'URL' refers to the url of the .mp4 file.
'driver_path' refers to the path of the Chrome driver used by Selenium.
'download_path' is the .mp4 file name and path to the .mp4 file (this is where the .mp4 file will be downloaded).

The funciton does not return anything but downloads the anime episode that the 'URL' variable has.

## dataScrapeFunctions.getEpisodesDF(df)
'df' refers to a dataframe that is specific to the a pandas.DataFrame containing a url(s) and other information and data pertaining to it.

The function returns another dataframe that contains the name of the anime and urls of the anime's episodes.

## dataScrapeFunctions.cleanShowUrls(listOfUrls)
'listOfUrls' refers to the list of urls that were submited by the user at the beginning of the program.
