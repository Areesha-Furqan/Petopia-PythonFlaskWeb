from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)



users = {} # variable initialization

if os.path.exists("users.json"): #  TO  CHECK  FILE  EXIST ????
    
    with open('users.json') as json_file: #   'with'  TO  CLOSE  FILE
        users = json.load(json_file) # USER  FILE  CONTENT -> CONVERT IN  PYTHON  FORMAT -> AND  SAVE

print(users) # TO  SHOW  IN  TERMINAL  



@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/adp')
def adp():
    return render_template('adp.html')



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': # USER  GIVES  INPUT (DATA) ???
        email = request.form['email']
        password = request.form['password']

        # CHECK  EMAIL  EXIST ???  PASWORD  MATCHES ???
        if email in users and users[email] == password:
            return redirect(url_for('home'))  # IF  HAVE -> GO  TO  HOME
        else:
            error_message = "Invalid email or password, please try again."
            return render_template('login.html', error=error_message) #
    
    return render_template('login.html')




#POST:  to  give  the  data  to  the  server

#GET:  to  SHOW  the  data(FORM)  to  the  USER  
@app.route('/reg', methods=['GET', 'POST']) 

def reg():
    if request.method == 'POST': #TO  CHECK  IF  THE  DATA  IS  SUBMITTED  BY  THE  USER
        email = request.form['email']
        password = request.form['password']
        
        
        #CHECKING  IF  THE  EMAIL  IS  ALREADY  EXITS
        if email in users:
            error_message = "Email already in use. Please try a different one."
            
            return render_template('reg.html', error=error_message)  # Pass error message to the template
        
        
        # TO ADD THE USER'S EMAIL & PASSWORD  IN  DICT
        
        users[email] = password # TO  SAVE  THE  VALUE  IN  THE  KEY  OF  DICTIONARY
        
        
        #SAVING  the  email  and  password  in  file(user.json) 
        with open('users.json', 'w') as json_file: # 'with'  TO  CLOSE  FILE  AUTOMATICALLY
                    
            json.dump(users, json_file, indent=4) # 'as json_file'  MEANS  'json_file='
                    #👆 GET DATA (FROM users) to send it in OBJECT ( json_file )
                        
            #👆DUMP is a function that takes Python data (like lists, dictionaries, etc.) and writes it to a file in JSON format.

        return redirect(url_for('login'))  # GET  THE  LOGIN  PAGE
    return render_template('reg.html')  # Render registration page






@app.route('/contact')  # Contact page
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
