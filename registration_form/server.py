from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def is_number(s):
    return any(i.isdigit() for i in s)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    #print request.form

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    passw = request.form['passw']
    confirm_passw = request.form['confirm_passw']

    flag = 0

    # first and last name, no numbers
    if len(first_name) < 1 or len(last_name) < 1:
        flash("Name fields cannot be empty")
        flag = 1
    # password more than 8
    if is_number(first_name) or is_number(last_name):
        flash("Name fields cannot include a number")
    if len(passw) <= 8:
        flash("Password must be longer than 8 characters")
        flag = 1
    if passw != confirm_passw:
        flash("Passwords do not match")
        flag = 1
    if flag == 1:
        return render_template('index.html', first_name = request.form['first_name'], last_name = request.form['last_name'])
        
    
    # all fields required
   
   
    # email valid
    # password and password confirmation match


    flash("Thanks for submitting your information!")
    return render_template('index.html')
    
app.run(debug=True)