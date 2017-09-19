# import libraries
import requests
import csv
from bs4 import BeautifulSoup

# gets Pitchfork review links and writes them to csv
def getReviewLinks(page_num):

	link_list = []

	# store URLs in a list, database has 1609 pages as of 9/15/2017
	
	page = requests.get("https://pitchfork.com/reviews/albums/?page=" + str(page_num))
	soup = BeautifulSoup(page.content, 'html.parser')
	review_list = soup.find_all(class_="album-link")
	
	i = 0
	while i < len(review_list):
		link_list.append(str(review_list[i]["href"]))
		i += 1
	
	return link_list




