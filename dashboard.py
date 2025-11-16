from flask import Flask, render_template, jsonify
import mysql.connector, json

config = json.load(open("config.json"))

db = mysql.connector.connect(
    host=config["DB_HOST"],
    user=config["DB_USER"],
    password=config["DB_PASS"],
    database=config["DB_NAME"]
)

cursor = db.cursor(dictionary=True)

app = Flask(__name__)

@app.route("/")
def home():
    cursor.execute("SELECT * FROM leads ORDER BY timestamp DESC")
    leads = cursor.fetchall()
    return render_template("dashboard.html", leads=leads)

@app.route("/chat/<lead_id>")
def chat(lead_id):
    cursor.execute("SELECT * FROM conversations WHERE lead_id=%s ORDER BY timestamp", (lead_id,))
    chats = cursor.fetchall()
    return render_template("chat.html", chats=chats)

app.run(port=5001)
