### Building URL Dynamically
### Variable Rule
### Jinja 2 Template Engine

'''
{{   }} Expressions to print output in HTML
{%...%} Conditions, For Loops
{#...#} Comments
'''

from flask import Flask, render_template, request, redirect, url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flash course!!</h1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submitold", methods=["GET", "POST"])
def submitold():
    if request.method == "POST":
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

## Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html', results=res)

## Variable Rule
@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score, 'res':res}
    return render_template('result1.html', results=exp)

## IF condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html', results=score)

## Dynamic URL
@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit', methods=["POST", "GET"])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        total_score = (science + maths) / 2
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=total_score)) 

if __name__ == "__main__":
    app.run(debug=True)
