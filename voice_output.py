import pyttsx3

def speak(text):
    if not text:
        return

    try:
        engine = pyttsx3.init()   # Initialize inside function
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        engine.say(str(text))
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print("Speech error:", e)



