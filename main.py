"""My first website"""
from flask import Flask, render_template, request

app = Flask(__name__)

"""This is for get method"""


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
