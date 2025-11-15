#bot.py

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# -----------------------
# Business info for Rimini PK
# -----------------------
MENU_PDF_URL = "https://drive.google.com/uc?export=download&id=1VJ3vqZScm0xJXT5CLMhOaMjymZFyn-2j"
OPENING_HOURS = "🕒 *Rimini PK Hours:*\nMonday–Sunday: 12 PM – 10 PM"
LOCATION = "📍 SS Tower Noor Mahal Road Bahawalpur  Pakistan."  # Replace with correct address
GREETING = (
    "Heyyy! Welcome to **Rimini PK** 🍦\n"
    "You can ask for: `menu`, `hours`, `location`."
)

# -----------------------
# Bot Route
# -----------------------
@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Greetings
    if incoming_msg in ["hi", "hello", "hey"]:
        msg.body(GREETING)

    # Menu PDF
    elif "menu" in incoming_msg:
        msg.body("Here’s our menu:")
        msg.media(MENU_PDF_URL)

    # Opening hours
    elif "hours" in incoming_msg or "opening" in incoming_msg:
        msg.body(OPENING_HOURS)

    # Location
    elif "location" in incoming_msg or "address" in incoming_msg:
        msg.body(LOCATION)

    # Unknown command
    else:
        msg.body(
            "Sorry, I didn't get that. You can ask for `menu`, `hours`, or `location`."
        )

    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
