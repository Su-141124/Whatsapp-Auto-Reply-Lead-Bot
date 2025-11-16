from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mysql.connector, json, datetime

config = json.load(open("config.json"))

db = mysql.connector.connect(
    host=config["DB_HOST"],
    user=config["DB_USER"],
    password=config["DB_PASS"],
    database=config["DB_NAME"]
)

cursor = db.cursor()

app = Flask(__name__)

def save_message(lead_id, msg, sender):
    cursor.execute(
        "INSERT INTO conversations(lead_id, message, sender) VALUES (%s,%s,%s)",
        (lead_id, msg, sender)
    )
    db.commit()

def get_or_create_lead(phone):
    cursor.execute("SELECT id FROM leads WHERE phone=%s", (phone,))
    res = cursor.fetchone()
    if res:
        return res[0]
    cursor.execute("INSERT INTO leads(name, phone) VALUES (%s,%s)", ("Unknown", phone))
    db.commit()
    return cursor.lastrowid

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body', '').lower()
    phone = request.form.get('From', '').replace("whatsapp:", "")

    lead_id = get_or_create_lead(phone)

    resp = MessagingResponse()
    msg = resp.message()

    save_message(lead_id, incoming_msg, "user")

    if "hi" in incoming_msg:
        reply = "Hello 👋! Welcome!
1. View Collections
2. Ask a Question
3. Contact Owner"
    elif incoming_msg == "1":
        reply = "We have: Silk Sarees, Cotton Sarees, Partywear."
    elif incoming_msg == "2":
        reply = "Ask your question!"
    elif incoming_msg == "3":
        reply = "Owner: +91XXXXXXXXXX"
    else:
        reply = "Thank you! We will contact you soon."

    msg.body(reply)
    save_message(lead_id, reply, "bot")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
