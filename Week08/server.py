from flask import Flask, url_for
from flask import request,redirect

app = Flask(__name__)
@app.route('/')
def index():
    #return "Hello, World!"
    redirect(url_for('login'))
@app.route('/login')

def Login():
    return "served by login"
    # to abort
    #abort(401)
#to route

@app.route('/user')
def getUser():
    return "server by getUser"
# pass a variable
@app.route('/user/<int:id>')
def findByIdUser(id):
    return "server by findByIdUsed"+str(id)

@app.route('/user', methods=['POST'])
def createUser():
    return "server by createUser"

@app.route("/demo_url_for")
def demoUrlFor():
    returnString ="url for index is"+ url_for("index")
    returnString += "<br/>"
    returnString +="url for find by id"+ url_for("findByIdUser", id=2)
    return returnString

@app.route("/demo_request", mothods=['POST','GET','DELETE'])
def demoRequest():
    return request.method

if __name__=="__main__":
    print("in if")
    app.run(debug=True)


