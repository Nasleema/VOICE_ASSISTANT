from datetime import datetime
import os


def log_interaction(command, response=None, status="recognized"):
    """
    Logs user command and system response with timestamp.
    
    Parameters:
    command (str): User spoken command
    response (str): System response
    status (str): recognized / unknown / timeout / exit
    """

    # Handle None safely
    command = command if command else "No input"
    response = response if response else "No response"

    # Generate timestamp
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get project base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ensure logs folder exists
    logs_dir = os.path.join(base_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Define log file path
    log_file_path = os.path.join(logs_dir, "command_log.txt")

    # Write structured log
    with open(log_file_path, "a", encoding="utf-8") as file:
        file.write(
            f"[{time_stamp}] "
            f"Command: {command} | "
            f"Response: {response} | "
            f"Status: {status}\n"
        )

