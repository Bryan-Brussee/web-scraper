import requests
import csv
from bs4 import BeautifulSoup
from scrape_page import scrapePage
from write_review_links import getReviewLinks


def getDatabase(start, end, operation):

	review_links = getReviewLinks(start, end)

	with open("data.csv", operation) as f:
	        writeFile = csv.writer(f, dialect="excel")
	        # writeFile.writerow(["Album", "Artist", "Genre", "Score", "Best New Music", "Reviewer", "Reviewer Detail", "Date", "URL"])
	        i = 0
	        while i < len(review_links):
	        	writeFile.writerows(scrapePage(review_links[i]))
	        	print("Scraping reviews: " + str(i + 1) + " of " + str(len(review_links)))
	        	i += 1
	f.close()




i = 131
while i <= 1500:
	getDatabase(i, i, "a")
	i += 1

# 130 pages of links