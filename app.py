from flask import Flask
from flask import render_template
app= Flask(__name__)

@app.route("/")
def get_index():
    return "<p>Hello there from my GitHub repo!</p>"
    

@app.route("/hello")   
def get_hello():
    return "<p> Hello and welcome to Flask</p>"
