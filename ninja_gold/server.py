from flask import Flask, render_template, request, redirect, session
import random
# import requests
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0

    if not 'activity' in session:
        session['activity'] = ''

    if not 'turns' in session:
        session['turns'] = 10

    if not 'highscore' in session:
        session['highscore'] = 0
    
    return render_template("index.html", gold = session['gold'], activity = session['activity'], turns = session['turns'], highscore = session['highscore'])


@app.route('/process_money', methods=['POST'])
def processMoney():

    print request.form
    print request.form['building']
    session['turns'] += -1
    building = request.form['building']
    print building
    print type(session['activity'])
    if building == 'farm':
        goldEarned = random.randrange(10,20)
        session['gold'] += goldEarned
        session['activity'] += "<p style='color:green;'>Earned "+ str(goldEarned)+" golds from the "+ str(building)+"</p>"
    elif building == "cave":
        goldEarned = random.randrange(5,10)
        session['gold'] += goldEarned
        session['activity'] += "<p style='color:green;'>Earned " + str(goldEarned)+" golds from the "+ str(building)+"</p>"
    elif building == "house":
        goldEarned = random.randrange(2,5)
        session['gold'] += goldEarned
        session['activity'] += "<p style='color:green;'>Earned " + str(goldEarned)+" golds from the "+ str(building)+"</p>"
    elif building == "casino":
        goldEarned = random.randrange(-50,50)
        session['gold'] += goldEarned
        if goldEarned < 0:
            session['activity'] += "<p style='color:red;'>LOST " + str(goldEarned)+" golds from the "+ str(building)+"</p>"
        elif goldEarned >= 0:
            session['activity'] += "<p style='color:green;'>Earned " + str(goldEarned)+" golds from the "+ str(building)+"</p>"
    # sends user back to root route
    if session['highscore'] < session['gold']:
        session['highscore'] = session['gold']
    if session['turns'] == 0:
        #session.clear()
        session['gold'] = 0
        session['activity'] = ''
        session['turns'] = 10
    

    return redirect('/')

app.run(debug=True)


#useful flask stuff pulled from documentation, web, and misc knowledge sources


#
# 
#@app.errorhandler(404)
#def page_not_found(error):
    #return render_template('page_not_found.html'), 404
#
#
# Request objects and session objects
#  class flask.Response(response=None, status=None, headers=None,mimetype=None, content_type=None, direct_passthrough=False)
# headers - a Headers object respresenting the response Headers
#
