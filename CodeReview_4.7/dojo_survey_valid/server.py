from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    print "test"
    #print request.form
    # request.form is a dictionary of values 

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash("Comment is not actually optional...")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Comment too long (120 character max)")
        return redirect('/')

    return render_template('result.html', name=name, location=location, language=language, comment=comment)
    
app.run(debug=True)