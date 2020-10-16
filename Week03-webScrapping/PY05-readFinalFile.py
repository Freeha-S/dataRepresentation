from bs4 import BeautifulSoup
import csv
with open("../Week2/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')
#print (soup.tr)
car_file = open('week02data.csv', mode='w')
car_writer = csv.writer(car_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
rows = soup.findAll("tr")
for row in rows:

   cols = row.findAll("td")
   dataList = []
   for col in cols:
      dataList.append(col.text)
   #write the all colums of data
   #car_writer.writerow(dataList)   

   car_writer.writerow(dataList[0:4]) # write the first four item of data from list.
car_file.close()