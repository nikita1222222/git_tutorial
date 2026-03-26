from flask import Flask, request

app= Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to first page'

@app.route('/api/')
def name():

    name = request.values.get('name')
    age = request.values.get('age')

    age = int(age)

    if age > 18:



        return "Welcome to the site,"+ name + '!'               ##To check the output you have to enter url like "http:/localhost:500/api?age=23&name=Nikita"
    else:
        return "Sorry, You are too young to access this site"
    
if __name__ == '__main__':

    app.run(debug=True)
        
