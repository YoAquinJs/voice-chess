"""
This module detects voice commands for a chess game using the Vosk speech recognition library.
It initializes the speech recognition model and listens for specific commands.
"""

import json
import logging
import numpy as np
import pyaudio
import vosk

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def initialize_model(model_path, sample_rate):
    """
    Initialize the Vosk speech recognition model and recognizer.

    Args:
        model_path (str): Path to the Vosk model directory.
        sample_rate (int): The audio sample rate in Hz.

    Returns:
        tuple: A tuple containing the model and the recognizer instance.
        Returns (None, None) if initialization fails.
    """
    try:
        model = vosk.Model(model_path)
        recognizer = vosk.KaldiRecognizer(model, sample_rate)
        return model, recognizer
    except AttributeError as error:
        logging.error("Error initializing model: %s", error)
        return None, None

def detect_prefix(recognizer, sample_rate):
    """
    Detect the audio input and return the recognized text.

    This function continuously listens for audio input, processes it using
    the Vosk recognizer, and returns the detected text when found.

    Args:
        recognizer (KaldiRecognizer): Vosk recognizer object to process audio.
        sample_rate (int): The audio sample rate in Hz.

    Returns:
        tuple: A boolean indicating if a command was detected, and the recognized text.
    """
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=sample_rate,
        input=True,
        frames_per_buffer=4096,
    )
    stream.start_stream()

    detected = False
    text = ""
    waiting_message_shown = False

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)

        if recognizer.AcceptWaveform(audio_data.tobytes()):
            result = recognizer.Result()
            text = json.loads(result).get("text", "").lower()

            if text:
                print(f"You said: {text}")
                detected = True
                break
        elif not waiting_message_shown:
            print("Waiting for the command to start recording...")
            waiting_message_shown = True

    stream.stop_stream()
    stream.close()
    p.terminate()

    return detected, text
