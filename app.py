import streamlit as st
from groq import Groq

# Page config
st.set_page_config(
    page_title="Virtual Darshan",
    page_icon="🤖",
    layout="centered"
)

# Load persona
with open("persona.txt", "r") as f:
    persona = f.read()

# Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Header
st.title("🤖 Virtual Darshan")
st.markdown("*AI-powered career assistant — ask me anything about Darshan's work, skills & projects*")
st.divider()

# Init chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    greeting = (
        "Hey there! 👋 I'm **Virtual Darshan** — an AI that represents "
        "Darshan Shetty, a Senior Product Manager with 8+ years of experience "
        "in e-commerce, D2C, logistics, and retail-tech.\n\n"
        "I'm here to answer any questions about Darshan's career, skills, "
        "projects, and interests. Whether you're a recruiter, hiring manager, "
        "or just curious — feel free to ask me anything! 🚀\n\n"
        "**Some things you can ask me:**\n"
        "- What's your experience in product management?\n"
        "- Tell me about your AI projects\n"
        "- Why are you targeting the UAE market?\n"
        "- What tools and tech do you work with?"
    )
    st.session_state.messages.append({
        "role": "assistant",
        "content": greeting
    })

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask Virtual Darshan something..."):

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": persona},
                *st.session_state.messages
            ],
            stream=True
        )
        reply = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in stream
        )

    st.session_state.messages.append({"role": "assistant", "content": reply})