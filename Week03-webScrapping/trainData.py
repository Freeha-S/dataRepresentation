import requests
import csv
from bs4 import BeautifulSoup
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
#print (soup.prettify())
#open the file to write
train_file= open('week03_train.csv', mode='w')
train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# use the list to retrive all tags
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

listings = soup.findAll("objTrainPositions")
for listing in listings:
    #print(listing)
    #print(listing.TrainLatitude.string)
    # can be used as well print(listing.find('TrainLatitude').string)
 #   entryList = []
  #  entryList.append(listing.find('TrainLatitude').string)

   #
   #  train_writer.writerow(entryList)

   ## to store trains that are south of Dublin, IE have a latitude less then that of Dublin (approx. 53.4)

   lat =float( listing.TrainLatitude.string)
   if (lat < 53.4):
        entryList = []
        for retrieveTag in retrieveTags:
            #print (listing.find(retrieveTag).string)
            entryList.append(listing.find(retrieveTag).string)
        train_writer.writerow(entryList)
train_file.close()



