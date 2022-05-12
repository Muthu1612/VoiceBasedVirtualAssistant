from vosk import Model, KaldiRecognizer
import pyaudio
import json
def listen():
    model = Model("model")
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    
    while True:
        data = stream.read(8192)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
        
            result = rec.Result()
            
            result = json.loads(result)
            text = result['text']

            return text
        
