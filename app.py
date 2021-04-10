from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("simple.html")


@app.route('/cat')
def cat_page():
    return "Here"  # render_template("pages/cat.html")


if __name__ == "__main__":
    app.run()
