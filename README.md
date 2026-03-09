🎧 AIVA – Assistive Intelligent Voice Assistant
Project Overview 🎯

AIVA (Assistive Intelligent Voice Assistant) is a Python-based voice assistant that enables users to interact with their computer using voice commands. The system supports tasks such as opening applications, performing voice-based calculations, searching YouTube, and typing text using speech.

The assistant is designed as an assistive technology solution, allowing users to perform computer operations without using a keyboard or mouse.

Use Cases: Assistive computing, hands-free interaction, accessibility support, educational demonstrations of voice systems.

🚀 Quick Start (5 Minutes)
1️⃣ Clone Repository
git clone https://github.com/yourusername/AIVA-Voice-Assistant.git
cd AIVA-Voice-Assistant

2️⃣ Setup Environment
python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application 🚀
streamlit run app.py

Open in browser:

http://localhost:8501

Click Start Listening and speak your command.

📊 System Capabilities
Feature	Description
Voice Commands	Perform system operations using speech
Voice Calculator	Solve mathematical expressions through voice
YouTube Voice Search	Search YouTube without typing
Voice Typing	Automatically type speech into Notepad
Command Logging	Records interactions for monitoring
Web Interface	Interactive dashboard built with Streamlit
🛠️ Technical Stack

Programming Language

Python

Libraries

Streamlit – User interface

SpeechRecognition – Speech-to-text

Pyttsx3 – Text-to-speech

PyAudio – Microphone access

PyAutoGUI – Voice typing automation

Development Tools

Python Virtual Environment

Git & GitHub

Streamlit Web Interface

📁 Project Structure

AIVA-Voice-Assistant

│
├── app.py

├── main.py

├── audio_capture.py

├── voice_output.py

├── response.py

├── logger.py

├── calculator_engine.py

├── responses.csv

├── requirements.txt

└── logs/


🎯 Key Features

✅ Voice-based application control

✅ Voice calculator for arithmetic operations

✅ Voice YouTube search without keyboard

✅ Speech-to-text typing in Notepad

✅ Command logging and monitoring

✅ Interactive Streamlit dashboard


🗺️ Development Workflow
Stage	Task
Planning	System architecture design
Implementation	Speech recognition & voice output modules
Integration	Command processing and automation
Interface	Streamlit dashboard development
Testing	Command accuracy and interaction logging
Deployment	Local Streamlit application


📈 Project Highlights

✔ Modular architecture for easy maintenance
✔ Hands-free interaction with computer systems
✔ Assistive technology concept for accessibility
✔ Integration of speech recognition and automation



📚 Example Voice Commands
Opening Applications
open google
open youtube
open notepad
Voice Calculator
eight plus three
10 divided by 2
50 minus 12
Voice Typing
open notepad
start speaking
stop typing


🎯 Use Cases

Assistive system for physically challenged users


Hands-free computing environments


Educational demonstration of voice-based systems


Prototype for smart assistants



🚀 Future Improvements

Continuous listening mode (like Alexa)


Advanced natural language processing


Integration with more applications


Smart home automation support
