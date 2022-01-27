from flask import Flask
from aws_credetianls import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY

#Defines te use of a flask app
app = Flask(__name__)

#Index flask route
@app.route("/")
def hello():
    if (AWS_SECRET_ACCESS_KEY != None and AWS_ACCESS_KEY != None):
        return ("Everything seems to be working for now...")
    else:
        return ("Something went wrong with your AWS credentials")

#run settings
app.run(host = '0.0.0.0', port = 80)