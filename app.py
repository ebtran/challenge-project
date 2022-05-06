from flask import Flask
from flask import render_template
import psycopg2
# import json

app = Flask(__name__)

# Database table
@app.route("/load_data")
def load_data():
    print("loading database...")
    try:
        conn = psycopg2.connect("host=db dbname=restsdb user=postgres password=secret")
    except:
        return "Unable to connect to database"
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS restaurants")
    cur.execute('''CREATE TABLE restaurants
        (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')
    print("Table created successfully")

    conn.commit()
    conn.close()
    
    # Number of rows
    nrows = 0
    # List of properties
    props = []
    return render_template("load_table.html", nrows=nrows, props=props)

# Homepage report
@app.route("/")
def home():
    return render_template("report.html")