"""My first website"""
from flask import Flask, render_template, request
# from pymongo import MongoClient

app = Flask(__name__)


# uri = "mongodb+srv://Doc:<password>@main.ob9pc3z.mongodb.net/"
# client = MongoClient(uri)
# db = client.get_database("Main")
# records = db["main"]


@app.route('/', methods=["GET"])
def login():
    """for login page"""
    return render_template("index.html")


@app.route('/LogIn', methods=["POST"])
def submit():
    """for submit page"""
    name = request.form.get('Email')
    passw = request.form.get('Password')
    # data = {
    #     "Email": name,
    #     "password": passw,
    # }
    # result = records.insert_one(data)
    # print("Inserted document ID:", result.inserted_id)
    if name == passw:
        return f"your Email is {name}, and your password is {passw}"
    else:
        return render_template("index1.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
