 #1. Create a Flask application with an /api route. When this route is accessed, 
#it should return a JSON list. The data should be stored in a backend file, read from it, 
#and sent as a response. 

from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    
    todays_date = datetime.now().strftime('%B %d, %Y')
    
    return render_template('index.html', day_of_week=day_of_week, todays_date=todays_date)

@app.route('/submit', methods= ['POST'])
def submit():

    name = request.form.get('name')
    
    print ("data submitted successfully")
    return 'Hello'
    

if __name__ == '__main__':
  app.run(debug=True)
