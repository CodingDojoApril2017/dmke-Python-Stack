from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'logindb')

@app.route('/')
def index():
    print "test my redirect"
    # SQL query to get all information from friends table
    query = "SELECT * FROM users"
    # function to query DB with SQL query 'query' as argument
    # setting variable friends to = return 
    loginreg = mysql.query_db(query)
    # render template with all_friends = to mysql db query
    return render_template('index.html', testmydb=loginreg)


def is_number(s):
    return any(i.isdigit() for i in s)

"""
@app.route('/')
def index():
    return render_template('index.html')
"""

@app.route('/register', methods=['POST'])
def register():
    
    print request.form

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    passw = request.form['passw']
    # only needed for validation, don't need in database
    confirm_passw = request.form['confirm_passw']
    #return redirect('/')
    flag = 0

    # first and last name, no numbers
    if len(first_name) < 2 or len(last_name) < 2:
        flash("Name fields cannot be empty")
        flag = 1
    # password more than 8
    if is_number(first_name) or is_number(last_name):
        flash("Name fields cannot include a number")
    # check for email, add valid email formatting later
    if len(email) < 3:
        flash("Email cannot be empty")
        flag = 1
    if len(passw) <= 8:
        flash("Password must be longer than 8 characters")
        flag = 1
    if passw != confirm_passw:
        flash("Passwords do not match")
        flag = 1
    if flag == 1:
        return redirect('/')
        #return render_template('index.html', first_name = #request.form['first_name'], last_name = request.form#['last_name'], email = request.form['email'])
        
    #information has been validated, store in database
    flash("Thanks for submitting your information!")

    #query into DB, insert information into table friends
    query = "INSERT INTO users (first_name, last_name, email, passw, created_at, updated_at) VALUES (:first_name, :last_name, :email, :passw, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email' : request.form['email'],
        'passw': request.form['passw']
    }
    # Run query with dictionary values in query, in this case query is an insert!
    mysql.query_db(query, data)
    return render_template('success.html')
    
app.run(debug=True)

"""
@app.route('/friends/<friend_id>')
def show(friend_id):
    #Query to select specific user by id. ':' and variable name to insert data
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # define a dictionary with key that matches :variable_name in query
    data = {'specific_id': friend_id}
    # run query with inserted data
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object
    return render_template('index.html', one_friend=friends[0])
"""
"""
@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, age = :age WHERE id = :id"
    
    data = {
        'first_name': request.form['first_name'], 
        'age' : request.form['age'],
        'id': friend_id
    }
    mysql.query_db(query, data) 
    return redirect('/')
"""
"""
@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/'
    )
""" 

"""
@app.route('/add', methods=['POST'])
def create():
    #query into DB, insert information into table friends
    query = "INSERT INTO friends (first_name, age, created_at, updated_at) VALUES (:first_name, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received
    data = {
        'first_name': request.form['first_name'],
        'age': request.form['age'],
    }
    # Run query with dictionary values in query
    mysql.query_db(query, data)
    return redirect('/')
"""

