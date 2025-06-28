
 🤖 InsureCoach AI

AI-Powered Insurance Sales Training Assistant

InsureCoach AI is an intelligent chatbot that helps insurance agents practice and perfect their pitch by simulating real-world customer interactions. Built with OpenAI’s GPT engine, it generates structured sales scripts tailored to different scenarios — instantly.

Whether you're preparing for a BFSI interview or training for a real client meeting, InsureCoach AI is your personal sales coach.

---

 🚀 What It Does

🧾 You type a scenario like:
> _"Train me to sell health insurance to a 30-year-old woman in Hyderabad who lives alone."_

✅ It replies with a structured pitch:

```

1. 🗣️ Greeting
   "Hi there! I help individuals like you plan for better healthcare security."

2. ❓ Discovery Questions
   "Have you considered any insurance plans before? What’s your biggest concern — premium, claims, or coverage?"

3. 💡 Product Pitch
   "Based on your age and profile, a ₹10L health insurance plan with cashless hospitalization would suit your needs."

4. 🤝 Closing Line
   "Would you like me to explain your top 2 options in a quick 10-minute call?"

5. ⚠️ Objection Handling
   "If she says 'It’s too early for me', respond with: 'The earlier you start, the lower the premium and better the benefits.'"

````

---

 💼 Why Use InsureCoach AI?

- 🎯 Trains agents with real-world sales conversations
- 🧠 AI-powered, context-aware, and realistic
- 📝 Saves hours on scriptwriting and coaching
- 🔄 Provides different strategies for different personas

---

 🛠️ Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| 💬 AI Model | OpenAI GPT-3.5 Turbo (via API) |
| 🌐 Backend  | Python + Flask + Flask-CORS    |
| 🎨 Frontend | HTML + CSS + Vanilla JS        |
| 🔐 Auth     | API Key via `.env` file        |

---

 🧪 How to Run Locally

 1️⃣ Backend Setup

```bash
pip install flask flask-cors python-dotenv requests
````

Create a file named `.env` inside the `backend/` folder and paste your [OpenAI API Key](https://platform.openai.com/account/api-keys):

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Start the Flask server:

```bash
python app.py
```

---

### 2️⃣ Frontend Setup

No installation needed. Just open the `login.html` file from the `templates/` folder in your browser.

---

## 💬 Example Inputs to Try

```txt
Train me to sell term insurance to a 45-year-old married man with two kids in Delhi.
```

```txt
How do I handle objections when a customer says insurance is too expensive?
```

```txt
Create a script to sell a retirement plan to a 60-year-old school teacher in Chennai.
```

---

 ✨ Features

* ✅ Structured output with Greeting, Questions, Pitch, Closing & Objections
* 🎯 Personalized responses for age, job, and location
* 🧠 Powered by ChatGPT-like API (OpenAI GPT-3.5)
* 🖥️ Responsive chat UI for live testing
* 💬 Bolded sections and bullet formatting for clarity

---

🏆 Ideal For

* 🔹 BFSI Interview Practice
* 🔹 Insurance Sales Agent Training
* 🔹 Role-Play Simulations
* 🔹 Hackathon Submissions (Internship Track)

---

 👤 Author

ISHIKA U. NAIK
June 2025

---

> ⚠️ Make sure you don’t share your OpenAI API key publicly. Keep your `.env` file private.

```

---

