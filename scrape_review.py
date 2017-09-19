# import libraries
# encoding=utf8

import requests
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str, smart_unicode
import sys

def scrapeReview(url): 

	reload(sys)
	sys.setdefaultencoding('utf8')

	# grab the page
	page = requests.get("https://pitchfork.com" + url)
	soup = BeautifulSoup(page.content, 'html.parser')

	# grab the html elements
	artists_soup = soup.find_all(class_="artists")
	genre_list = soup.find_all(class_="genre-list__link")
	bnm_raw = soup.find_all(class_="score-box")
	author = soup.find(class_="authors-detail__display-name").get_text()
	author_detail = soup.find(class_="author_detail__display-name")
	date = soup.find(class_="pub-date")

	# album list
	albums = [i.get_text() for i in soup.find_all(class_="review-title")]
	artist = []
	scores = [float(i.get_text()) for i in soup.find_all(class_="score")]
	bnm_list = []
	genre = " ,".join([i.get_text() for i in soup.find_all(class_="genre-list__link")])

	# get album data
	i = 0
	while i < len(albums):

		# jump through some hoops to make sure artists' names come in right
		artist_a_elements = artists_soup[i].find_all('a')
		name_list = [a.get_text() for a in artist_a_elements]
		name_string = "/".join(name_list)
		artist.append(name_string)

		# fairly straight forward gathering of album names and scores

		# tag best new music and best new reissues
		if bnm_raw[i]["class"][1] == "bnm":
			status = soup.find_all(class_=("bnm-txt"))
			bnm_list.append(status.pop(0).get_text())
		else:
			bnm_list.append("")
		i += 1

	# pull author data	
	if author_detail == None:
		author_detail = ""
	else:
		author_detail = author_detail.get_text()

	# get the date attribute from the time tag
	date = str(date['title'])

	# store the data in a list
	data = []
	i = 0
	while i < len(albums):
		data.append([albums[i], artist[i], genre, scores[i], bnm_list[i], author, author_detail, date, url])
		i += 1

	return(data)

test = scrapeReview("/reviews/albums/22393-unfinished-music-no-1-two-virgins-unfinished-music-no-2-life-with-the-lions-yoko-ono-plastic-ono-band/")
print(test)
