import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#print (soup.prettify())
# get the property card list

listings = soup.findAll("div", class_="PropertyListingCard" )
for listing in listings:
    entry = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entry.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entry.append(address)
    #print(entry)

    home_writer.writerow(entry)
home_file.close()