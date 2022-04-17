import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import time
import os
# import pyttsx3
from keras.models import load_model
model = load_model('model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))



import tkinter
from tkinter import *




base = Tk()
base.title("Agent")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)


ChatLog = Text(base, bd=0, bg="red", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)


scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

def send():
    msg=EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END,"Me :"+ msg + '\n\n')
        
        with open("agent.txt","w") as a:
            a.write(msg)

        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)




EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")



SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

def send2(msg):

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Customer: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)




scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

#base.mainloop()
to_talk=""
base.update_idletasks()
base.update()

while True:
    base.update_idletasks()
    f= open("customer.txt","r+")
    content=f.read()
    if content!="":
        send2(content)
        f.truncate(0)
    f.close()
    base.update()

    

