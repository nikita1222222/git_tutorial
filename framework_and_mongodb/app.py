from flask import Flask,request,render_template                        ## Import from Flask module
from datetime import datetime                                          ##import datetime module

app= Flask(__name__)                             ##create a Flask Application

@app.route('/')                                  ##Define a home path/route by '/' 
def home():                                      ##create a home function
    day_of_week= datetime.now().strftime('%A')   ##call the module, result will show in backend
    #day= datetime.now().strftime('%a')
    #print(day_of_week)
    #print(day)
    current_datetime= datetime.now()
    today_date= current_datetime.strftime('%d/%m/%Y')
    current_time= datetime.now().strftime('%H:%M:%S')
                                        
    return render_template('index.html', day_of_week=day_of_week, today_date=today_date, current_time=current_time) ##when we want to define and run variable in front end of flask we have to use {{}} brases. jinja2

@app.route('/api/<name>')      ##Getting a value
def name(name):


    return 'Welcome to the second page'

@app.route('/submit', methods=['POST'])
def submit():
    
    name = request.form.get('name')
    print(request.args)
    return "Hello, " + name + '!'

if __name__ == '__main__':                       ##you have to call this to run the application
    app.run(debug=True)                           ## debug==true required to check for the changes in the code