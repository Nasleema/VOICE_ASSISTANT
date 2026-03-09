from audio_capture import capture_audio
from logger import log_interaction
from response import generate_response
from voice_output import speak
from calculator_engine import calculate_expression

import webbrowser
import os
import datetime
import pyautogui


def run_assistant_once():

    command = capture_audio(timeout=15)

    if command is None:

        reply = "No input detected."
        speak(reply)
        log_interaction("No Input", reply, "timeout")
        return reply, "timeout"

    cmd = command.lower().strip()


    # EXIT
    if any(word in cmd for word in ["exit", "stop", "quit"]):

        reply = "Goodbye!"
        speak(reply)
        log_interaction(command, reply, "exit")
        return reply, "exit"


    # TIME
    if "time" in cmd:

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        reply = f"The current time is {current_time}"


    # DATE
    elif "date" in cmd:

        current_date = datetime.datetime.now().strftime("%d %B %Y")
        reply = f"Today's date is {current_date}"


    # OPEN GOOGLE
    elif "open google" in cmd:

        webbrowser.open("https://www.google.com")
        reply = "Opening Google."


    # OPEN YOUTUBE WITH VOICE SEARCH
    elif "open youtube" in cmd:

        speak("What do you want to search on YouTube?")

        search_query = capture_audio()

        if search_query:

            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)

            reply = f"Searching YouTube for {search_query}"

        else:

            reply = "I did not hear the search query."


    # OPEN CALCULATOR MODE
    elif "open calculator" in cmd:

        speak("Calculator mode activated. Say your calculation.")

        calc_command = capture_audio()

        if calc_command:

            result = calculate_expression(calc_command)

            if result is not None:
                reply = f"The answer is {result}"
            else:
                reply = "Sorry, I could not calculate that."

        else:

            reply = "No calculation detected."


    # OPEN NOTEPAD WITH VOICE TYPING
    elif "open notepad" in cmd:

        os.system("notepad")

        speak("Notepad opened. Start speaking to type. Say stop typing to end.")

        while True:

            speech = capture_audio()

            if speech is None:
                continue

            if "stop typing" in speech:
                reply = "Stopping dictation."
                break

            pyautogui.write(speech + " ")


    # DIRECT CALCULATION COMMAND
    elif any(word in cmd for word in ["plus","minus","times","divided","multiplied","add","subtract"]):

        result = calculate_expression(cmd)

        if result is not None:
            reply = f"The answer is {result}"
        else:
            reply = "Sorry, I could not calculate that."


    # OTHER RESPONSES
    else:

        reply = generate_response(command)

        if not reply:

            reply = "I did not understand that command."
            speak(reply)
            log_interaction(command, reply, "unknown")
            return reply, "unknown"


    speak(reply)
    log_interaction(command, reply, "recognized")

    return reply, "recognized"







