# Import Beautiful Soup package.
from bs4 import BeautifulSoup

# Open the file from week 2 lab.
with open("../Week2/carviewer2.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')

 #print (soup.prettify())

# # Print first <tr> from the file.
# print(soup.tr)

# Extract and print all the <tr> part 5.
# rows = soup.findAll("tr")
# for row in rows:
#     print("------")
#     print(row)


# # For each row, get contents of <td> part 6.
# rows = soup.findAll("tr")
# for row in rows:
#     print("------")
#     cols = row.findAll("td")
#     for col in cols:
#         print(col.text)
# For each row, store text from columns in a list.
rows = soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    dataList = [] #empty list
    for col in cols:
        dataList.append(col.text)# append the column data to list
    print (dataList)# print the data of the row