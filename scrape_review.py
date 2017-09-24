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
	bnm_soup = soup.find_all(class_="score-box")
	author = soup.find(class_="authors-detail__display-name").get_text()
	author_detail = soup.find(class_="authors-detail__title")

	# album list
	albums = [i.get_text() for i in soup.find_all(class_="review-title")]
	artist = []
	genre = " ,".join([i.get_text() for i in soup.find_all(class_="genre-list__link")])
	scores = [float(i.get_text()) for i in soup.find_all(class_="score")]
	bnm_list = []
	date = str(soup.find(class_="pub-date")["title"])

	# get album data
	i = 0
	while i < len(albums):

		# jump through some hoops to make sure artists' names come in right
		artist_li_elements = artists_soup[i].find_all('li')
		name_list = [li.get_text() for li in artist_li_elements]
		name_string = "/".join(name_list)
		artist.append(name_string)

		# tag best new music and best new reissues
		if bnm_soup[i]["class"][1] == "bnm":
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

	# store the data in a list
	data = []
	i = 0
	while i < len(albums):
		data.append([albums[i], artist[i], genre, scores[i], bnm_list[i], author, author_detail, date, url])
		i += 1

	return(data)


# test cases

# various artists tag
# test = scrapeReview("/reviews/albums/16926-just-tell-me-that-you-want-me-tribute-to-fleetwood-mac/")
# print(test)

# # multiple artist attribution
# test = scrapeReview("/reviews/albums/22393-unfinished-music-no-1-two-virgins-unfinished-music-no-2-life-with-the-lions-yoko-ono-plastic-ono-band/")
# print(test)
