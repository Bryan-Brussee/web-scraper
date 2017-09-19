# import libraries
# encoding=utf8

import requests
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str, smart_unicode
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def scrapeReview(url): 
	# grab the page
	page = requests.get("https://pitchfork.com" + url)
	soup = BeautifulSoup(page.content, 'html.parser')

	# grab the html elements
	artists_list = soup.find_all(class_="artists")
	albums_raw = soup.find_all(class_="review-title")
	genre_list = soup.find_all(class_="genre-list__link")
	scores_raw = soup.find_all(class_="score")
	bnm_raw = soup.find_all(class_="score-box")
	author_raw = soup.select("a.authors-detail__display-name")
	author_detail_raw = soup.select("span.authors-detail__title")
	date_raw = soup.select("time.pub-date")

	# album list
	albums = []
	artist = []
	scores = []
	bnm_list = []
	genre = []
	data = []


	# get album data
	i = 0
	while i < len(albums_raw):

		# jump through some hoops to make sure artists' names come in right
		artist_a_elements = artists_list[i].find_all('a')
		name_list = [a.get_text() for a in artist_a_elements]
		name_string = "/".join(name_list)
		artist.append(name_string)

		# fairly straight forward gathering of album names and scores
		albums.append(albums_raw[i].get_text())
		scores.append(float(scores_raw[i].get_text()))

		# tag best new music and best new reissues
		if bnm_raw[i]["class"][1] == "bnm":
			status = soup.find_all(class_=("bnm-txt"))
			bnm_list.append(status.pop(0).get_text())
		else:
			bnm_list.append("")
		i += 1


	# build genre list
	i = 0
	while i < len(genre_list):
		genre.append(genre_list[i].get_text())
		i += 1
	genre = ", ".join(genre)

	# pull author data
	author = author_raw[0].get_text()
	if len(author_detail_raw) > 0:
		author_detail = author_detail_raw[0].get_text()
	else:
		author_detail = ""

	# get the date attribute from the time tag
	time_tag = date_raw[0]
	date = str(time_tag['title'])

	# store the data in a list
	data = []
	i = 0
	while i < len(albums):
		data.append([albums[i], artist[i], genre, scores[i], bnm_list[i], author, author_detail, date, url])
		i += 1

	return(data)


