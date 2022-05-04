from flask import Flask
from flask import render_template

app = Flask (__name__)

# Database table
@app.route("/load_data")
def load_data():
    return render_template("load_table.html")

# Homepage report
@app.route("/")
def home():
    return render_template("report.html")