# import libraries
import requests
import csv
from bs4 import BeautifulSoup

# grab the page
page = requests.get("https://pitchfork.com/reviews/albums/mount-kimbie-love-what-survives/")
soup = BeautifulSoup(page.content, 'html.parser')

# grab the html elements
score_raw = soup.select("span.score")
bnm_raw = soup.select("p.bnm-txt")
album_raw = soup.select("h1.review-title")
artist_raw = soup.select("ul.artist-list li  a")
genre_list = soup.find_all(class_="genre-list__link")
author_raw = soup.select("a.authors-detail__display-name")
author_detail_raw = soup.select("span.authors-detail__title")
date_raw = soup.select("time.pub-date")

# get text from elements
score = float(score_raw[0].get_text())
album = str(album_raw[0].get_text())
artist = str(artist_raw[0].get_text())
author = str(author_raw[0].get_text())
author_detail = str(author_detail_raw[0].get_text())

# check best new music status
if len(bnm_raw) > 0:
	bnm = str(bnm_raw[0].get_text())
else:
	bnm = "none"

# loop through genres to build a list
genre = []
i = 0
while i < len(genre_list):
	genre.append((str(genre_list[i].get_text())))
	i += 1

# get the date attribute from the time tag
time_tag = date_raw[0]
date = str(time_tag['title'])

# print results
print(artist, album, genre, score, bnm, author, author_detail, date)


# goes back to page 1608






