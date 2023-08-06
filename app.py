from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def time():
    now = datetime.now(timezone('Asia/Kolkata'))
    return "the current date and time in siliguri is{}".format(now)