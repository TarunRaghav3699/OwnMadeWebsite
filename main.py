"""My first website"""
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


uri = "mongodb+srv://mongotarun:2TGYh1qmeaYcnKjR@cluster0.w31imin.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.get_database("main")
records = db["MyRecords"]


@app.route('/', methods=["GET"])
def login():
    """for login page"""
    return render_template("index.html")


@app.route('/LogIn', methods=["POST"])
def submit():
    """for submit page"""
    name = request.form.get('Email')
    passw = request.form.get('Password')
    if name == passw:
        return f"your Email is {name}, and your password is {passw}"
    else:
        return render_template("index1.html")


if __name__ == "__main__":
    app.run(port=5001)
