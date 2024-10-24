"""
This module controls a chess game using voice commands.
It uses a voice detector to start the game, move pieces, and end
the game with 'checkmate'. It also integrates with TTS (text-to-speech)
to provide verbal feedback to the user.
"""

import json
import logging
import time

import tts
import voice_detector
from chess_commands import (
    COMMAND_CHECKMATE,
    COMMAND_CHESS,
    COMMAND_STARTGAME,
)

# Configure logging for the module
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config():
    """
    Load configuration settings from the JSON file.

    Returns:
        dict: A dictionary containing configuration settings such as
        the model path and sample rate.
    """
    with open("config.json", encoding="utf-8") as config_file:
        config = json.load(config_file)
    return config

def main():
    """
    Main function to run the voice-controlled chess game.

    This function initializes the voice detector model, waits for commands
    like 'start game', 'chess', and 'checkmate', and performs appropriate actions
    using TTS (text-to-speech).
    """
    config = load_config()
    model_path = config["MODEL_PATH"]
    sample_rate = config["SAMPLE_RATE"]
    recognizer = voice_detector.initialize_model(model_path, sample_rate)[1]

    if recognizer is None:
        logging.error("Failed to initialize the model.")
        return

    game_started = False

    while True:
        if not game_started:
            detected, text = voice_detector.detect_prefix(recognizer, sample_rate)

            if detected and COMMAND_STARTGAME in text:
                print("The game has started!")
                tts.speak("The game has started!")
                game_started = True
                time.sleep(2)  # Prevent audio capture from TTS

        if game_started:
            detected, text = voice_detector.detect_prefix(recognizer, sample_rate)

            if detected:
                if COMMAND_CHECKMATE in text:
                    tts.speak("Checkmate! The game is over.")
                    print("Game ended with checkmate")
                    break  # Exit the main loop when "checkmate" is detected

                # Detect the word 'chess' to start recording the next command
                if COMMAND_CHESS in text:
                    print("Chess detected")
                    tts.speak("What is your next move?")
                    time.sleep(2)

                    # Record the user's move command (e.g., "e4")
                    detected, command_text = voice_detector.detect_prefix(recognizer, sample_rate)

                    if detected and command_text:
                        print(f"Your move was: {command_text}")
                        tts.speak(f"Your move was: {command_text}")

                else:
                    print(f"You said: {text}")  # Log any non-command detected text


if __name__ == "__main__":
    main()
