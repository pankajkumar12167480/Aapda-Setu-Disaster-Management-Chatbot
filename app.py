from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "No message provided."})
    
    user_msg = data["message"]
    bot_reply = chatbot_response(user_msg)
    return jsonify({"reply": bot_reply})

# Render will set the PORT automatically using gunicorn
if __name__ == "__main__":
    app.run(debug=True)
