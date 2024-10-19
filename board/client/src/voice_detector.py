# voice_detector.py
import json
import vosk
import pyaudio
import numpy as np

def initialize_model(model_path, sample_rate):
    try:
        model = vosk.Model(model_path)
        recognizer = vosk.KaldiRecognizer(model, sample_rate)
        return model, recognizer
    except AttributeError as e:
        print(f"Error initializing model: {e}")
        return None, None

def detect_prefix(model, recognizer, sample_rate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=4096)
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
                if "chess" in text:
                    detected = True
                    break
                elif "stop" in text:
                    print("Stopping the program as requested.")
                    detected = False
                    break
        elif not waiting_message_shown:
            print("Waiting for the word 'chess' to start recording...")
            waiting_message_shown = True

    stream.stop_stream()
    stream.close()
    p.terminate()

    return detected, text









