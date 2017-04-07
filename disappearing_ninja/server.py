from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/result', methods=['GET', 'POST'])
def result():
    print "Got GET info"
    #print request.form
    # request.form is a dictionary of values 

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template('result.html', name=name, location=location, language=language, comment=comment)
""" 
@app.route('/ninja/')
def ninjas():
    return render_template('ninja.html', color="default")

@app.route('/ninja/<color>')
def route_ninja(color):
    print color
    return render_template('ninja.html', color=color)

app.run(debug=True)