
#2. Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas. 
#Upon successful submission, the user should be redirected to another page displaying the message 
#"Data submitted successfully". If there's an error during submission, display the error on the same 
#page without redirection.

from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
#import requests
import os
import pymongo

load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


#uri = "mongodb://patilnikita830_db_user:Dpsh0hmYc9hSnArY@ac-dl9q06v-shard-00-00.rqahs9e.mongodb.net:27017,ac-dl9q06v-shard-00-01.rqahs9e.mongodb.net:27017,ac-dl9q06v-shard-00-02.rqahs9e.mongodb.net:27017/?ssl=true&replicaSet=atlas-avo5pj-shard-0&authSource=admin&appName=Mongoproject1"

mongo_uri=os.getenv('mongo_uri')

# Create a new client and connect to the server
client = pymongo.MongoClient(mongo_uri)

db= client.test

collection = db['mongo-tutorial']

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime("%A")
    todays_date = datetime.now().strftime("%B %d, %Y")
    return render_template('index.html', day_of_week=day_of_week, todays_date=todays_date)

@app.route('/submit', methods=['POST'])
def submit():

    form_data= dict(request.form)

    collection.insert_one(form_data)

    return 'Data Submitted Successfully'

if __name__=="__main__":
    app.run(debug=True)







