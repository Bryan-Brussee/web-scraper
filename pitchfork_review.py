# import libraries
import requests
from bs4 import BeautifulSoup

# grab the page
page = requests.get("https://pitchfork.com/reviews/albums/sparks-hippopotamus/")
soup = BeautifulSoup(page.content, 'html.parser')

# grab the html elements
score_raw = soup.select("span.score")
album_raw = soup.select("h1.review-title")
artist_raw = soup.select("ul.artist-list li  a")
genre_list = soup.find_all(class_="genre-list__link")

# clean html elements
score = score_raw[0].get_text()
album = album_raw[0].get_text()
artist = artist_raw[0].get_text()
genre = []
i = 0
while i < len(genre_list):
	genre.append((str(genre_list[i].get_text())))
	i += 1

# print results
print(artist)
print(album)
print(score)
print(genre)





