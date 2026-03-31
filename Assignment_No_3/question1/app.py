#1. Create a Flask application with an /api route. When this route is accessed, 
#it should return a JSON list. The data should be stored in a backend file, read from it, 
#and sent as a response. 


from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():

    day = datetime.today().strftime('%A')
    date = datetime.today()
    return render_template('index.html', day=day, date=date)


@app.route('/api')
def name():

    name = request.values.get('name')
    age = request.values.get('age')

    age = int (age)
    result = {
        'name': name, 
        'age': age,
    }
    return result

if __name__=="__main__":
    app.run(debug=True)