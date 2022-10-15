from flask import Flask, render_template, url_for
from flask import request, redirect, abort, make_response
from flask import g, session, flash
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
