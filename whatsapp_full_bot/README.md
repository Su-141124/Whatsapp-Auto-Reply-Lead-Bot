🚀 WhatsApp Auto-Reply + Lead Management Bot

AI-powered WhatsApp Assistant + Customer Lead Tracking Dashboard.

📌 Overview :-

This is a full-stack WhatsApp Auto-Reply + Lead Management System built using:

Flask (backend for WhatsApp bot)

Twilio WhatsApp API (message automation)

MySQL Database (lead + chat storage)

Admin Dashboard (view leads & their conversations)

It acts like a mini CRM tool for small shops, boutiques, parlours, and service providers.

You can deploy this for 2–3 customers as a mini product!

🎯 Features:-

🤖 WhatsApp Bot

Auto-replies to customers

Sends menu options

Handles user choices

Stores conversations

Saves phone numbers automatically as leads

🗂️ Lead Management System:-

Stores all leads in MySQL

Saves:

Name

Phone

Interest/product

Timestamp

🖥️ Admin Dashboard:-

View all leads

View complete chat history

Clean and simple UI

Works on localhost or server

🧠 Extensible:-

You can easily add:

AI FAQ answering

Product catalog

Image sending

Auto follow-up system

🏗️ Project Architecture:-

Customer WhatsApp Message
          ↓
   Twilio WhatsApp API
          ↓
    Flask Backend (app.py)
          ↓
  MySQL Database (store leads + chats)
          ↓
Admin Dashboard (dashboard.py)

📁 Folder Structure
whatsapp_full_bot/
│── app.py                 # WhatsApp bot backend
│── dashboard.py           # Admin dashboard (Flask)
│── config.json            # Database credentials
│── schema.sql             # MySQL DB schema
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── templates/
│     ├── dashboard.html   # Lead table UI
│     └── chat.html        # Chat history UI


💬 Example WhatsApp Flow

User: Hi
Bot:

Hello 👋! Welcome!
1. View Collections
2. Ask a Question
3. Contact Owner


User: 1
Bot:

We have:
- Silk Sarees
- Cotton Sarees
- Partywear

🖥️ Dashboard Screenshots

(You can replace these with real images after you run the project)

📌 Lead Table
ID | Name | Phone | Interest | Time | Chat

💬 Chat History
User: hi
Bot: Hello! Welcome…
User: 1
Bot: We have silk, cotton…

🚀 Future Enhancements (You Can Add Easily) :-

Add login system for admin

Automatic follow-up reminders

AI-powered FAQ (OpenAI / Llama)

Send product images automatically

Add product catalog page in dashboard

Export leads to Excel
