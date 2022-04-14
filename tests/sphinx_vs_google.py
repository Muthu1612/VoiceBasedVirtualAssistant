
import speech_recognition as sr
import datetime

r = sr.Recognizer()


with sr.Microphone() as source:
    
    
    while True:
        audio = r.listen(source)

        
        google = r.recognize_google(audio)
        sphinx = r.recognize_sphinx(audio)

        print('Google: [{}]\nSphinx: {}\n\n'.format(google, sphinx))
