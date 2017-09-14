# import libraries
import requests
from bs4 import BeautifulSoup

def scrapePage(url): 
	# grab the page
	page = requests.get(url)
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
	artist = str(artist_raw[0].get_text())

	# album list
	albums = []
	scores = []
	bnm_list = []
	genre = []
	data = []


	i = 0
	while i < len(albums_raw):
		albums.append(str(albums_raw[i].get_text()))
		scores.append(float(scores_raw[i].get_text()))
		bnm_list.append(str(bnm_raw[i]["class"][1]))
		i += 1

	# build genre list
	i = 0
	while i < len(genre_list):
		genre.append(str(genre_list[i].get_text()))
		i += 1

	# pull author data
	author = str(author_raw[0].get_text())
	author_detail = str(author_detail_raw[0].get_text())

	# get the date attribute from the time tag
	time_tag = date_raw[0]
	date = str(time_tag['title'])

	# store the data in a list
	data = []
	i = 0
	while i < len(albums):
		data.append([artist, albums[i], genre, scores[i], bnm_list[i], author, author_detail, date])
		i += 1

	return(data)











