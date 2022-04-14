
# Import libraries

#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import pyttsx3

from core import SystemInfo


from nlu.classifier import classify


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()



model = Model("model")
rec = KaldiRecognizer(model, 16000)


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
speak("Hello, How may I help you?")
print("Hello, How may I help you?")


while True:
    
    data = stream.read(8192)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        
        result = rec.Result()
        
        result = json.loads(result)
        text = result['text']

        entity = classify(text)

        if entity == 'time\\getTime':
            temp1=SystemInfo.get_time()
            print(temp1)
            speak(SystemInfo.get_time())
        if entity == 'time\\getDate':
            temp2=SystemInfo.get_date()
            print(temp2)
            speak(SystemInfo.get_date())
        elif entity == 'time\\getYear':
            temp3=SystemInfo.get_year()
            print(temp3)
            speak(SystemInfo.get_year())
        elif entity == 'close\\exit':
            print("Thank you for contacting me")
            speak("Thank you for contacting me")
            exit()
        else:
            pass

        print('You said: ', text)