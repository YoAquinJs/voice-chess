"""
This module provides text-to-speech functionality using the pyttsx3 library.
"""

import pyttsx3

def speak(text):
    """
    Convert the given text to speech.

    Args:
        text (str): The text to be spoken aloud.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
