from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = { 'username' : 'Jayson'}
    posts = [
        {'author' : {'username' : 'Maria'}, 'body' : "Olá mundo!"},
        {'author' : {'username' : 'José'}, 'body' : "Olá galera!"},
    ]
    return render_template("index.html", user = user, posts = posts)
