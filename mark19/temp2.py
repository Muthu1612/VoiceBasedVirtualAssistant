import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import time
import os
import pyttsx3
from keras.models import load_model
model = load_model('model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words



def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    if len(return_list)>0:
        return return_list 
    else:
        os.system("cls")
        print("list len is 0")
        return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res,ints



import tkinter
from tkinter import *




base = Tk()
base.title("Customer")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)


ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)


scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

def send():
    
    msg=EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)


    global human
    
    if human==True:
        with open("customer.txt","w") as c:
            c.write(msg)

        with open("agent.txt","r+") as a:
            temp=""
            while temp=="":
                time.sleep(0.5)
                temp=a.read()
            ans=temp[temp.find(":")+1:]
            ChatLog.insert(END,"Agent :"+ ans + '\n\n')
            a.truncate(0)
        int=temp[0:temp.find(":")]
        data_file = open('intents.json').read()
        intents2 = json.loads(data_file)
        temp_dict=            {"tag": int,
        "patterns": [msg],
        "responses": [ans],
        "context": [""]
        }
        intents2.update(temp_dict)
        with open('intents.json', 'w') as json_file:
            json.dump(intents2, json_file)
        
        
        return 



    if msg != '':
        
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res,no_use = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

# def human(intents):
#         print("Connecting to human....")
#         print("Type answer ")
#         answer=EntryBox.get("1.0",'end-1c').strip()
#         ChatLog.insert(END, "Bot: " + res + '\n\n')
            
#         ChatLog.config(state=DISABLED)
#         ChatLog.yview(END)
#         print("Type intent")
#         intent=EntryBox.get("1.0",'end-1c').strip()



EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")



SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

def send2(msg):
   

    if msg != '':
        
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))


        res,ints = chatbot_response(msg)
        # global intents
        tag = ints[0]['intent']
        # list_of_intents = intents['intents']
        # for i in list_of_intents:
        if(tag=="human_interference"):
            ChatLog.insert(END, "Connecting.... " +'\n\n')
            human=True
            return
                
              
        

        
        ChatLog.insert(END, "Bot: " + res + '\n\n')
       
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        return res



scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

#base.mainloop()
to_talk=""
human=False
while True:
    
    base.update_idletasks()
    if human==False:
        f=open("text_and_status.txt","r+")
        text=f.read()
        if text!="":
            to_talk=send2(text)
            f.truncate(0)
        f.close()

    base.update()
    if to_talk!="" and human!=True:
        speak(to_talk)
        to_talk=""
