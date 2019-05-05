import requests
# import MySQLdb
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#SQL connection data to connect and save the data in
HOST = "34.74.36.56"
# USERNAME = "scraping_user"
# PASSWORD = ""
# DATABASE = "scraping_sample"

#URL to be scraped
url_to_scrape = 'https://events.cornell.edu/'
# query the website and return the html to the variable ‘page’
page = urlopen(url_to_scrape)
#parse the data
soup = BeautifulSoup(page, "html.parser")

event_list = soup.find_all("div", {"class": "item event_item vevent"})

#Iterate through each event
for item in event_list:
    #Get title
    title = item.find("h3").text
    print(title)

    # Get location and remove trailing and leading spaces
    location = item.find("div", {"class": "location"}).text.strip()
    print(location)

    # Get and split date and time
    date_time = item.find("abbr", {"class": "dtstart"}).text.split()
    full_date = date_time[0].split('/')
    # Store date and time values
    month = full_date[0]
    day = full_date[1]
    year = full_date[2]
    time = date_time[1]

    print(day, month, year)
    print(time)

    # Get full description
    event_url = item.find("h3", {"class": "summary"}).find("a")['href']
    event_page = urlopen(event_url)
    event_soup = BeautifulSoup(event_page, "html.parser")
    
    full_descr = event_soup.find("div", {"class": "description"}).text
    print(full_descr)

    # Get and split categories
    categories = item.find("div", {"class": "event_filters"}).text.split(", ")
    # Since there are too many categories to keep track of
    # we will take the primary category
    # Remove all spaces to split by "/"
    primary_category = categories[0].replace(" ", "").split("/")[0]
    print(primary_category)