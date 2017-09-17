import requests
import csv
from bs4 import BeautifulSoup
from scrape_page import scrapePage
from write_review_links import writeReviewLinks

a = writeReviewLinks(1, 2)

pages = []

with open("data.csv", "wb") as f:
        writeFile = csv.writer(f, dialect="excel")
        i = 0
        while i < len(a):
        	writeFile.writerows(scrapePage(a[i]))
        	print("Scraping reviews: " + str(i + 1) + " of " + str(len(a)))
        	i += 1

