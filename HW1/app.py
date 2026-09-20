from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    hobbies = ["헬스", "음악 듣기", "회화 공부"]
    return render_template("profile.html", hobbies=hobbies)