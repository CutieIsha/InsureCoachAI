import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
    app.run(debug=True, port=5000)
