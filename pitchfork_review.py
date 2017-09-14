# import libraries
import requests
from bs4 import BeautifulSoup

# grab the page
page = requests.get("https://pitchfork.com/reviews/albums/hundred-waters-communicating/")
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
i = 0
while i < len(albums_raw):
	albums.append(str(albums_raw[i].get_text()))
	i += 1

# genre list
genre = []
i = 0
while i < len(genre_list):
	genre.append(str(genre_list[i].get_text()))
	i += 1

# scores list
scores = []
i = 0
while i < len(scores_raw):
	scores.append(float(scores_raw[i].get_text()))
	i += 1

# check best new music status
bnm_list = []
i = 0
while i < len(bnm_raw):
	bnm_list.append(str(bnm_raw[i]["class"][1]))
	i += 1

author = str(author_raw[0].get_text())
author_detail = str(author_detail_raw[0].get_text())

# get the date attribute from the time tag
time_tag = date_raw[0]
date = str(time_tag['title'])

# print results
i = 0
while i < len(albums):
	print(artist, albums[i], genre, scores[i], bnm_list[i], author, author_detail, date)
	i += 1


# goes back to page 1608






