from flask import Flask, render_template
app = Flask(__name__)

@app.route ("/")
def home():
    return "Hola Mundo"

@app.route ("/inicio/")
def index():
    return render_template("index.html")
