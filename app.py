from flask import Flask, render_template
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def time():
    now = datetime.now(timezone('Asia/Kolkata'))
    return render_template("index.html", cow=now)