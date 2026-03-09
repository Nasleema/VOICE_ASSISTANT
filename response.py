import csv
import os
import random


def load_responses():
    responses = {}

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "responses.csv")

    try:
        with open(csv_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                command_key = row.get("command", "").lower().strip()
                response_value = row.get("response", "").strip()

                if not command_key or not response_value:
                    continue

                if command_key not in responses:
                    responses[command_key] = []

                responses[command_key].append(response_value)

    except Exception as e:
        print("Error loading CSV:", e)

    return responses


# Load responses once
RESPONSES = load_responses()


def generate_response(user_command):
    if not user_command:
        return None

    user_command = user_command.lower().strip()

    # Split user command into words
    user_words = user_command.split()

    for key, values in RESPONSES.items():
        key_words = key.split()

        # Check if all words in key exist in user command
        if all(word in user_words for word in key_words):
            return random.choice(values)

    # Intelligent fallback
    return "I am still learning. Could you please rephrase your question?"



