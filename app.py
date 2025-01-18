from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)



users = {} # variable initialization

with open('users.json') as json_file:
    users = json.load(json_file)
print(users)



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



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists and the password matches
        if email in users and users[email] == password:
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            error_message = "Invalid email or password, please try again."
            return render_template('login.html', error=error_message)  # Pass error message to the template
    
    return render_template('login.html')  # Render login page on GET request




@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if the email already exists
        if email in users:
            error_message = "Email already in use. Please try a different one."
            return render_template('reg.html', error=error_message)  # Pass error message to the template
        
        # Add user to the dictionary
        users[email] = password
        success_message = "Registration successful! Please log in."
        print(" 54 users", users)
        with open('users.json', 'w') as json_file:
            json.dump(users, json_file, indent=4)            

        return redirect(url_for('login', success=success_message))  # Redirect to login page with success message
    
    
    return render_template('reg.html')  # Render registration page




@app.route('/contact')  # Contact page
def contact():
    return render_template('contact.html')

@app.route('/welcome')  # Welcome page after successful login
def welcome():
    username = request.args.get('username')
    return f"Welcome, {username}! You are logged in."

if __name__ == '__main__':
    app.run(debug=True)
