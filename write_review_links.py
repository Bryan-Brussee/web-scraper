# import libraries
import requests
import csv
from bs4 import BeautifulSoup

# gets Pitchfork review links and writes them to csv
def getReviewLinks(start, end):

	link_list = []

	# store URLs in a list, database has 1609 pages as of 9/15/2017
	
	while start <= end:
		page = requests.get("https://pitchfork.com/reviews/albums/?page=" + str(start))
		soup = BeautifulSoup(page.content, 'html.parser')
		review_list = soup.find_all(class_="album-link")
		
		i = 0
		while i < len(review_list):
			link_list.append(str(review_list[i]["href"]))
			i += 1
		print("Gathering links: " + str(start) + " of " + str(end))
		start += 1

	return link_list




