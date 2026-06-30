# 🤖 Virtual Darshan — AI Career Chatbot

A locally-developed, cloud-deployed AI persona that answers questions about Darshan Shetty's career, skills, projects, and interests. Built as part of an AI PM portfolio to demonstrate end-to-end product thinking and hands-on AI development.

**🔗 Live Demo: [virtual-darshan-chatbot.streamlit.app](https://virtual-darshan-chatbot.streamlit.app/)**

---

## 💡 What Is This?

Virtual Darshan is a conversational AI chatbot that acts as an interactive version of my resume. Instead of a static PDF, recruiters and hiring managers can have a real conversation — asking about my experience, projects, skills, and why I'm targeting the UAE market.

---

## 🧠 Product Thinking Behind It

| Decision | Rationale |
|---|---|
| Local-first development with Ollama | Privacy-first — no data leaves the machine during development |
| Groq API for production | Sub-2 second response time on free tier |
| Prompt-level guardrails | Keeps the bot on-scope without doubling LLM calls |
| Streamlit for UI | Fastest path from Python script to shareable web app |
| Streamlit Cloud for hosting | Zero-cost deployment with no DevOps overhead |

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| LLM (local dev) | Ollama + LLaMA 3.2 |
| LLM (production) | Groq API + LLaMA 3.3 70B |
| Frontend | Streamlit |
| Guardrails | Prompt engineering |
| Hosting | Streamlit Cloud (free tier) |
| Version control | GitHub |

---

## 🏗️ Architecture

```
User Question
     ↓
Streamlit Web UI
     ↓
System Prompt (persona.txt) + Guardrail Instructions
     ↓
Groq API — LLaMA 3.3 70B
     ↓
Streamed Response → Chat UI
```

**Guardrail logic** is baked directly into the system prompt — the model silently checks if a question is within scope before answering. Out-of-scope questions return a fixed deflection message instantly.

---

## 🚀 Run Locally

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed with `llama3.2` model pulled

### Setup

```bash
# Clone the repo
git clone https://github.com/darshanshetty10/virtual-darshan.git
cd virtual-darshan

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run locally with Ollama
ollama serve                             # make sure Ollama is running
python -m streamlit run app.py
```

---

## ☁️ Deploy to Production (Free)

1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → New App
3. Select repo → `main` branch → `app.py`
4. Add secret in Advanced Settings:
   ```
   GROQ_API_KEY = "your-groq-api-key"
   ```
5. Deploy — live in ~2 minutes

---

## 📁 Project Structure

```
virtual-darshan/
├── app.py            # Streamlit web app
├── chatbot.py        # Local CLI version (Ollama)
├── persona.txt       # Career context + guardrail instructions
├── requirements.txt  # Dependencies
└── README.md
```

---

## 💬 Sample Questions to Ask

- *What's your experience in product management?*
- *Tell me about your AI projects*
- *Why are you targeting the UAE market?*
- *What tools and tech do you work with?*
- *Walk me through your career path*

---

## 👤 About Darshan

Senior Product Manager with 8+ years across B2C/B2B e-commerce, D2C brands, logistics, and retail-tech. Currently based in Mumbai, targeting Senior PM roles in the UAE.

- 🔗 [LinkedIn](https://www.linkedin.com/in/darshanshetty)
- 💻 [GitHub](https://github.com/darshanshetty10)
- 🤖 [Live Chatbot](https://virtual-darshan-chatbot.streamlit.app/)

---

## 📌 Part of AI PM Portfolio

This project is part of a broader AI portfolio built to demonstrate practical AI product development skills:

- ✅ **Virtual Darshan** — AI career chatbot (this project)
- 🔄 **AI Job Hunter** — Automated job search pipeline (Python + n8n + Groq)

---

*Built with zero cloud cost. Runs LLaMA 3.3 70B via Groq API on Streamlit Cloud free tier.*
