# import libraries
# encoding=utf8

import requests
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str, smart_unicode
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def scrapePage(url): 
	# grab the page
	page = requests.get("https://pitchfork.com" + url)
	soup = BeautifulSoup(page.content, 'html.parser')

	# grab the html elements
	artist_raw = soup.select("ul.artist-list li  a")
	albums_raw = soup.find_all(class_="review-title")
	genre_list = soup.find_all(class_="genre-list__link")
	scores_raw = soup.find_all(class_="score")
	bnm_raw = soup.find_all(class_="score-box")
	author_raw = soup.select("a.authors-detail__display-name")
	author_detail_raw = soup.select("span.authors-detail__title")
	date_raw = soup.select("time.pub-date")


	# artist string
	artist = artist_raw[0].get_text()

	# album list
	albums = []
	scores = []
	bnm_list = []
	genre = []
	data = []


	i = 0
	while i < len(albums_raw):
		albums.append(albums_raw[i].get_text())
		scores.append(float(scores_raw[i].get_text()))
		# bnm_list.append(bnm_raw[i]["class"][1])
		if bnm_raw[i]["class"][1] == "bnm":
			status = soup.find_all(class_=("bnm-txt"))
			bnm_list.append(status[i].get_text())
		else:
			bnm_list.append("")
		i += 1

	# build genre list
	i = 0
	while i < len(genre_list):
		genre.append(str(genre_list[i].get_text()))
		i += 1

	# pull author data
	author = author_raw[0].get_text()
	author_detail = author_detail_raw[0].get_text()

	# get the date attribute from the time tag
	time_tag = date_raw[0]
	date = str(time_tag['title'])

	# store the data in a list
	data = []
	i = 0
	while i < len(albums):
		data.append([albums[i], artist, genre, scores[i], bnm_list[i], author, author_detail, date])
		i += 1

	return(data)



