import speech_recognition as sr
import pyttsx3 
import requests
import json
from requests.auth import HTTPBasicAuth
import ensurepip
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser 
import pyaudio
import wikipedia
import os
from gtts import gTTS



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[0].id)  # 0-male voice , 1-female voice
def speak(audio):   
    engine.say(audio)    
    engine.runAndWait() 

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
          speak("Good Morning!")    
    
    elif hour>=12 and hour<18:
          speak("Good Afternoon!")       
    
    else:
          speak("Good Evening!")  
        
   
    speak('I am Alfred, your Artificial intelligence assistant. Please tell me how may I help you ')

def translate_to_tamil(MyText):
            data1 ={"text": [MyText], "model_id":"en-ta"}
            url1="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b1c22bd7-bb2f-4f6e-b9ec-08cdd7f99de0"
            header1= {"Content-Type": "application/json"}
            user1= {"apikey":"KEq1BcZYYDhfSWn4vnnnkCaligSOpSidDjtVucL-HPnk"}
            obj=requests.post(url=url1,json=data1,headers=header1,auth = HTTPBasicAuth('apikey', 'KEq1BcZYYDhfSWn4vnnnkCaligSOpSidDjtVucL-HPnk'))
            # print("type: ",type(obj.content))
            # print(obj.content,"\n\n\n\n")
            res=(obj.content).decode('utf-8')
            sentences=json.loads(res)["translations"]
            print(sentences)
            for x in sentences:
                TTS = gTTS(text=x["translation"], lang='ta')
                TTS.save("voice.mp3")
                os.system("start voice.mp3")
                print(x["translation"])
                # SpeakText(x["translation"])

def translate_to_jap(MyText):
            data1 ={"text": [MyText], "model_id":"en-ja"}
            url1="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b1c22bd7-bb2f-4f6e-b9ec-08cdd7f99de0"
            header1= {"Content-Type": "application/json"}
            user1= {"apikey":"KEq1BcZYYDhfSWn4vnnnkCaligSOpSidDjtVucL-HPnk"}
            obj=requests.post(url=url1,json=data1,headers=header1,auth = HTTPBasicAuth('apikey', 'KEq1BcZYYDhfSWn4vnnnkCaligSOpSidDjtVucL-HPnk'))
            # print("type: ",type(obj.content))
            # print(obj.content,"\n\n\n\n")
            res=(obj.content).decode('utf-8')
            sentences=json.loads(res)["translations"]
            print(sentences)
            for x in sentences:
                print(x["translation"])
                SpeakText(x["translation"])

def takecommand():  
    global MyText
    r=sr.Recognizer()
    with sr.Microphone() as source2:
        
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            

            try:                                            # error handling
                print('Recognizing...')
                print(f"User said " + MyText )
                speak(MyText)

                if 'wikipedia' in MyText :
                    speak('Searching Wikipedia....')
                    MyText = MyText.replace('wikipedia','')
                    results = wikipedia.summary(MyText, sentences = 5)
                    print(results)
                    speak(results)
                elif 'translate' and 'tamil' in MyText:
                    t_text=translate_to_tamil(MyText)
                    speak(t_text)          

                elif 'translate' and 'japanese' in MyText:
                    t_text=translate(MyText)
                    speak(t_text)  
                elif 'open youtube' in MyText :
                    webbrowser.open('youtube.com')

                elif 'open google' in MyText :
                    webbrowser.open('google.com')

                elif 'time' in MyText :
                    strtime = datetime.datetime.now().strftime('%H:%M:%S')
                    speak(f'Sir the time is {strtime}')


                elif 'open stack overflow' in MyText :
                    webbrowser.open('stackoverflow.com')

                elif 'open free code camp' in MyText :
                    webbrowser.open('freecodecamp.org')

    
                elif 'exit' in MyText:
                    speak('okay boss, please call me when you need me')
                    quit()


                
            except Exception as e :
                print('Say that again please...')
                speak("can you repeat pleas")        # 'say that again' will be printed in case of improper voice
                return 'None'  
    return MyText



if __name__ == '__main__' :                      # execution control
    greet()
    while True:
        takecommand()
        # The whole logic for execution of tasks based on user asked MyText

    
    
      







