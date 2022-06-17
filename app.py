from flask import Flask
from flask import render_template
from flask import redirect
app= Flask(__name__)

@app.route("/")           
def get_index():
    return "<p>Hello there from my GitHub repo!</p>"
    

@app.route("/hello")   
def get_hello():
    return render_template('hello.html', name = "Art")


@app.route("/charisse")   
def get_charisse():
    return render_template('hello.html', name = "Charisse")

@app.route("/hi")
@app.route("/hi/")
@app.route("/hi/<name>")   
def get_hi(name="Izzy"):
    return render_template('hello.html', name = "name")


@app.route("/login", methods=["GET"])
def get_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def get_login():
    return render_template("hello.html", name="new login")


