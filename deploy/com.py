
# Import libraries

#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
# import os
# import subprocess
import pyaudio
import json
# import pyttsx3
# Import the core lib
# from core import SystemInfo
# from core.system import Runner

# # Runner
# runner = Runner()

# # Speech Synthesis
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# model = Model("High_spec_model")
model = Model("model")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# speak("Hello, How may I help you?")
# print("Hello, How may I help you?")
def listen():
    stream.start_stream()
    
    while True:
        data = stream.read(8192)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
        
            result = rec.Result()
            
            result = json.loads(result)
            text = result['text']

            # print(result['result'])
            # print(text)
            return text
        
# while True:
#     text=listen()
#     with open("text_and_status.txt","w") as f:
#         f.write(text)
    # f=open("speak.txt","r+")
    # text=f.read()
    # if text!="":
    #     speak(text)
    #     f.truncate(0)
    # f.close()

# WARNING (VoskAPI:LinearCgd():optimization.cc:549) 
# Doing linear CGD in dimension 100, after 15 iterations the squared residual has got worse, 
# 2.25951 > 1.55819.  Will do an exact optimization.