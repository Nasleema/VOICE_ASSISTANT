import streamlit as st
from main import run_assistant_once
import os

st.set_page_config(
    page_title="AIVA - Voice Assistant",
    page_icon="🎧",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.25);
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

/* Chat Bubble */
.chat-bubble {
    background: rgba(255,255,255,0.25);
    padding: 15px 20px;
    border-radius: 15px;
    margin-top: 10px;
    font-size: 17px;
}

/* BUTTON STYLE */
.stButton > button {
    background-color: #2c2c2c;
    color: white;
    font-size: 18px;
    font-weight: 600;
    border-radius: 12px;
    height: 50px;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #444;
}

/* Text Color */
h1, h2, h3, p {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎧 AIVA Assistant")
st.sidebar.caption("Smart Conversational Voice System")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Logged Commands", "About"]
)

# ---------------- LOG FILE PATH ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "logs", "command_log.txt")

# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.title("🎧 AIVA - Voice Assistant")
    st.write("Your modular conversational assistant with live voice interaction.")

    # ---------- CONTROL PANEL ----------
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("Control Panel")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Start Listening", use_container_width=True):

            with st.spinner("Listening... Speak now"):

                reply, status = run_assistant_once()

            # Save response
            st.session_state.chat_history.append(reply)

    with col2:

        if st.button("Stop Listening", use_container_width=True):

            st.success("Assistant stopped")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- CONVERSATION ----------
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("Conversation")

    if st.session_state.chat_history:

        for message in st.session_state.chat_history:

            st.markdown(
                f'<div class="chat-bubble">🤖 {message}</div>',
                unsafe_allow_html=True
            )

    else:
        st.info("Press 'Start Listening' and speak your command.")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- SYSTEM STATUS ----------
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.subheader("System Status")
    st.success("System Ready")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# LOGGED COMMANDS
# =====================================================

elif page == "Logged Commands":

    st.title("Logged Commands")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = file.readlines()

        if logs:

            for line in reversed(logs[-20:]):
                st.write(line)

        else:
            st.info("No commands logged yet.")

    else:
        st.warning("Log file not found.")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# ABOUT
# =====================================================

elif page == "About":

    st.title("About AIVA")

    st.markdown("""
**AIVA (Assistive Intelligent Voice Assistant)**

A modular conversational voice assistant built using:

• Speech Recognition  
• Text-to-Speech  
• Python  
• Streamlit UI  

The system captures voice commands, processes them, generates responses,
and logs interactions for analysis.

This assistant supports:

- Voice commands
- Voice calculator
- YouTube voice search
- Voice typing for disabled users
""")

    








