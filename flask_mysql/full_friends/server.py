from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'myfriendsdb')

@app.route('/')
def index():
    # SQL query to get all information from friends table
    query = "SELECT * FROM friends"
    # function to query DB with SQL query 'query' as argument
    # setting variable friends to = return 
    friends = mysql.query_db(query)
    # render template with all_friends = to mysql db query
    return render_template('index.html', all_friends=friends)

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

app.run(debug=True)