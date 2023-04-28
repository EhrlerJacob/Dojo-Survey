from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/create', methods=['POST'])
def create_user():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/users/show_user')

@app.route('/users/show_user')
def show_user():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True, port = 5000)
