import speech_recognition as sr

def capture_audio(timeout=15):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nAdjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening... (You have 15 seconds)")
        try:
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=timeout
            )
        except sr.WaitTimeoutError:
            print("No speech detected within 30seconds.")
            return None

    try:
        print("Processing speech...")
        text = recognizer.recognize_google(audio)

        cleaned_text = text.lower().strip()
        print(f"Recognized Text: {cleaned_text}")

        return cleaned_text

    except sr.UnknownValueError:
        print("Speech was unclear. Please try again.")
        return None

    except sr.RequestError:
        print("Could not connect to speech recognition service.")
        return None


# For testing this module independently
if __name__ == "__main__":
    result = capture_audio()

    if result:
        print("Final Output:", result)
    else:
        print("No valid input captured.")



