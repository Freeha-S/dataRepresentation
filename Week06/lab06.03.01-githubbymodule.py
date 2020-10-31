from github import Github
import requests
# remove the minus sign from the key
g = Github("7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0")
# get repo name
for repo in g.get_user().get_repos():
 print(repo.name)
# get the clone url of the repository aPrivateOne
repo = g.get_repo("datarepresentationstudent/aPrivateOne")
print(repo.clone_url)
#  get the download url of the file in this repository called test.txt
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)
# Use the download_url to make a http request to the file can output the contents of the file(TEXT contents).
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)
# Append the text more stuff (with a newline character) to the contents of the file.
newContents = contentOfFile + " more stuff \n"
#print (newContents)
# Update the contents of the file on git up by using the function 
#update_file(path, message, content, sha, branch=NotSet, committer=NotSet, author=NotSet)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
