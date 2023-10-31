"""My first website"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = "GDtfD^&$%@^8tgYjD"


uri = f"mongodb+srv://Test:{os.getenv('MONGODB_PASSWORD')}@main.l0zlzdr.mongodb.net/"
client = MongoClient(uri)
db = client.get_database("Main")
records = db["test"]



@app.route('/', methods=['GET'])
def index():
    """redirect me to login page"""
    return render_template("index.html")

@app.route('/templates/dashboard.html', methods=['GET'])
def dashboard():
    """redirect me to login page"""
    return render_template("dashboard.html")

@app.route('/dashboard', methods=["GET"])
def login():
    """redirect me to dashboard"""
    return render_template("Dashboard.html")

@app.route('/LogIn', methods=['POST'])
def login_db():
    """if the user data is in database then show me the advertisement"""
    name = request.form.get("Email")
    passw = request.form.get('Password')

    user_data = db.test.find_one({'Email' : name})

    if user_data is None:
        return redirect(url_for('signup'))
    if passw == user_data['password']:
        session['name'] = name
        return redirect(url_for("test"))
    return "Incorrect Password"

@app.route('/test')
def test():
    return f"welcome {session.get['name']}"

@app.route('/SignUp', methods=['POST'])
def submit():
    """to add the user data to database and redirect to the advertisement"""
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
        return render_template("tarun.html")


@app.route('/Signup', methods=['GET'])
def signup():
    """
    redirect me to the signup page
    """
    return render_template('index2.html')





if __name__ == "__main__":
    app.run(port=5001, debug=True)
