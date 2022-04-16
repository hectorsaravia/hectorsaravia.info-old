from flask import Flask, make_response, send_from_directory
from aws_credetianls import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY, BUCKET_NAME, OBJECT_NAME, FILE_NAME
import boto3, os

#Declaration of AWS credentials to use the s3 resource
s3 = boto3.client('s3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name='sa-east-1'
)

#downloads the file

#Defines te use of a flask app
app = Flask(__name__)

#Index flask route
@app.route("/")
def hello():
    if (AWS_SECRET_ACCESS_KEY != None and AWS_ACCESS_KEY != None):
        s3.download_file(BUCKET_NAME,OBJECT_NAME,'/CV.pdf')
        return send_from_directory('/', 'CV.pdf')
    else:
        return ("Something went wrong with your AWS credentials")

#run settings
app.run(host = '0.0.0.0', port = 80)