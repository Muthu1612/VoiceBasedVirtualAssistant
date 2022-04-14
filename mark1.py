import speech_recognition as sr
import pyttsx3 
import requests
import json
from requests.auth import HTTPBasicAuth

r = sr.Recognizer() 
  

def SpeakText(command):
      

    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

  
while(1):    

    try:
          

        with sr.Microphone() as source2:
              

            r.adjust_for_ambient_noise(source2, duration=0.2)
              
           
            audio2 = r.listen(source2)
              
  
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
  
            print("Did you say "+MyText)
            SpeakText(MyText)
            # data1 ={"text": ["Hello, world.", "How are you?"], "model_id":"en-ta"}
            data1 ={"text": [MyText], "model_id":"en-ta"}
            url1="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/8efcce74-6d07-4060-a852-ca5ed1f34fc4/v3/translate?version=2018-05-01"
            header1= {"Content-Type": "application/json"}
            user1= {"apikey":"CC_5o39gSACcmgq-JMcYtpkgkGrI7A9DXw5B2f9y_iJ9"}
            obj=requests.post(url=url1,json=data1,headers=header1,auth = HTTPBasicAuth('apikey', 'CC_5o39gSACcmgq-JMcYtpkgkGrI7A9DXw5B2f9y_iJ9'))
            # print("type: ",type(obj.content))
            # print(obj.content,"\n\n\n\n")
            res=(obj.content).decode('utf-8')
            # with open("out2.txt","w",encoding="utf-8") as file:
            #     file.write(res)



            sentences=json.loads(res)["translations"]
            print(sentences)
            for x in sentences:
                print(x["translation"])
                SpeakText(x["translation"])

            if MyText=="yes":
                print("Nice")
                SpeakText("cool")
            if MyText=="stop":
                print("Ok Bye")
                SpeakText(" At your command Master")
                
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")