
#f = open("../week2/carviewer2.html", "r")
#html = f.read()
#print (html)

#read from file using api key
import requests
import json
#html = '<h1>hello world</h1>This is html'
apiKey= '7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0'
url = 'https://api.github.com/user/repos'
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print (response.json())
filename = "lab06.02.json"
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

