"""My first website"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)


uri = f"mongodb+srv://Test:{os.getenv('MONGODB_PASSWORD')}@main.l0zlzdr.mongodb.net/"
client = MongoClient(uri)
db = client.get_database("Main")
records = db["test"]



@app.route('/', methods=['GET'])
def dashboard():
    """adding a modal"""
    return render_template("index.html")

@app.route('/dashboard', methods=["GET"])
def login():
    """for login page"""
    return render_template("dashboard.html")

@app.route('/LogIn', methods=['POST'])
def login_db():
    """to check if the users data is already present in the database"""
    name = request.form.get("Email")
    passw = request.form.get('Password')

    user_data = db.test.find_one({'Email' : name})

    if user_data is None:
        return redirect(url_for('signup'))
    if passw == user_data['password']:
        return render_template("tarun.html")
    return "Incorrect Password"


@app.route('/SignUp', methods=['POST'])
def submit():
    """for submit page"""
    idemail = request.form.get('Email')
    name = request.form.get('Name')
    username = request.form.get('Username')
    passw = request.form.get('Password')

    data = {
        "Email": idemail,
        "Full Name": name,
        "Username": username,
        "password": passw,
    }
    result = records.insert_one(data)
    print("Inserted document ID:", result.inserted_id)

    if name == passw:
        return f"""your Email is {name}, and your password is {passw},
        these both can't be same so please change your password"""
    else:
        return render_template("dashboard.html")


@app.route('/Signup', methods=['GET'])
def signup():
    """
    for sign up
    """
    return render_template('index2.html')





if __name__ == "__main__":
    app.run(port=5001, debug=True)
