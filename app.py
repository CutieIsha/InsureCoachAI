import os
import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/loginBtn", methods=["POST"])
def handle_login():
    # You can add login validation here
    return redirect(url_for('home'))

@app.route("/mentor")
def mentor():
    return render_template("index.html")


@app.route("/api/respond", methods=["POST"])
def respond():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        formatted_prompt = f"""
You are a professional sales training coach helping new insurance agents learn how to pitch.
Always structure your answer clearly in the following format:

1. 🗣️ **Greeting**
2. ❓ **Discovery Questions**
3. 💡 **Product Pitch**
4. 🤝 **Closing Line**
5. ⚠️ **Objection Handling Tips**

Now respond to this sales scenario:
\"\"\"{prompt}\"\"\"
"""

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful insurance sales training coach."},
                    {"role": "user", "content": formatted_prompt}
                ]
            }
        )

        if response.status_code != 200:
            print("❌ OpenAI Error:", response.text)
            return jsonify({"reply": "Sorry, OpenAI API failed to respond."})

        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        print("❌ Exception in backend:", str(e))
        return jsonify({"reply": "Something went wrong. Please try again."})

if __name__ == "__main__":
    # Use environment PORT or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)