#main.cpp
import voice_detector
import stt_tts
import config
import time

def main():
    model_path = config.MODEL_PATH
    sample_rate = config.SAMPLE_RATE

    #inicialización del modelo a traves de voice_detector
    model, recognizer = voice_detector.initialize_model(model_path, sample_rate)
    
    #verificar si el modelo se cargó correctamente
    if model is None or recognizer is None:
        print("Failed to initialize the model.")
        return
    
    while True:
        detected, text = voice_detector.detect_prefix(model, recognizer, sample_rate)
        
        if detected:
            print("The word 'chess' was detected, starting command recording...")
            stt_tts.speak("What is your next command?")
            time.sleep(2)  #agregar tiempo para que no capture el audio del TTS
        else:
            if "stop" in text:
                stt_tts.speak("Stopping the program.")
                break
        
        if text and 'chess' not in text and "stop" not in text:
            print(f"Processed command: {text}")
            stt_tts.speak(f"Command received was: {text}")
            break

if __name__ == "__main__":
    main()




