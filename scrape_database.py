import requests
import csv
from bs4 import BeautifulSoup
from scrape_review import scrapeReview
from get_review_links import getReviewLinks


def scrapeAlbumReviewPage(page):

	review_links = getReviewLinks(page)

	with open("data.csv", "a") as f:
	        writeFile = csv.writer(f, dialect="excel")
	        # writeFile.writerow(["Album", "Artist", "Genre", "Score", "Best New Music", "Reviewer", "Reviewer Detail", "Date", "URL"])
	        i = 0
	        while i < len(review_links):
	        	writeFile.writerows(scrapeReview(review_links[i]))
	        	print("Scraping reviews: " + str(i + 1) + " of 12")
	        	i += 1
	f.close()



def scrapeDatabase(start, end):

	i = start
	while i <= end:
		print("Gathering links: Page " + str(i) + " of " + str(end))

		scrapeAlbumReviewPage(i)
		print("Page "+ str(i) + " scraped.")
		i += 1

scrapeDatabase(2, 50)

