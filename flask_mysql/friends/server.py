from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    #Query to DB
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    # Run query with dictionary values in query
    mysql.query_db(query, data)
    return redirect('/')

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

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    
    data = {
        'first_name': request.form['first_name'], 
        'last_name' : request.form['last_name'],
        'occupation': request.form['occupation'],
        'id': friend_id
    }
    mysql.query_db(query, data) 
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/'
    )
app.run(debug=True)