# import libraries
import requests
from bs4 import BeautifulSoup

# grab the page
page = requests.get("https://pitchfork.com/reviews/albums/tori-amos-native-invader/")
soup = BeautifulSoup(page.content, 'html.parser')

# grab the html elements
score_raw = soup.select("span.score")
album_raw = soup.select("h1.review-title")
artist_raw = soup.select("ul.artist-list li  a")
genre_list = soup.find_all(class_="genre-list__link")
author_raw = soup.select("a.authors-detail__display-name")
date_raw = soup.select("time.pub-date")

# get text from elements
score = score_raw[0].get_text()
album = album_raw[0].get_text()
artist = artist_raw[0].get_text()
author = author_raw[0].get_text()

# loop through genres to build a list
genre = []
i = 0
while i < len(genre_list):
	genre.append((str(genre_list[i].get_text())))
	i += 1

# get the date attribute from the time tag
time_tag = date_raw[0]
date = time_tag['title']




# print results
print(artist)
print(album)
print(score)
print(genre)
print(author)
print(date)









