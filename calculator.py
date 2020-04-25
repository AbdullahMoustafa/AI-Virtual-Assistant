# import speech_recognition as sr
# import datetime
# from datetime import date
# import webbrowser
# import os
# import smtplib 
# from gtts import gTTS
# import pyttsx3 
# from pyttsx3 import voice
# import requests
# from pprint import pprint
import re
import math

def Sum(x,y):
    ans = x+y
    return ans
def multiply(x,y):
    ans = x*y
    return ans
def subtract(x,y):
    ans = x-y
    return ans
def divide(x,y):
    ans = x/y
    return ans
def power(x,y):
    ans = x**y
    return ans

#one operand
def sin(x):
    ans = math.sin((math.pi/180)*x)
    return round(ans,3)

def cos(x):
    ans = math.cos((math.pi/180)*x)
    return round(ans,3)

def tan(x):
    ans = math.tan((math.pi/180)*x)
    return round(ans,3)

# print(cos(30))
#Test calculator feature 
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #1/0 for female/male
engine.setProperty('rate',150)
engine.setProperty('volume',1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('Im ready sir')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
    try:
        print("Recognizing!")
        query = r.recognize_google(audio,language='en')
        print(f"user said:{query}\n")
        print("the queue is "+ str(query))
    except Exception as e:
        print("Say it again please")
        query = None
        print("the queue is "+ str(query))

    return query

speak("How can I help you")
query= takeCommand()

while(query != None):

    if ('calculate') in query.lower():
        speak("Working on it...")
        string = query
        #calculate 10 + 10 
        string = re.findall('\d+', string)

        operand1 = int(string[0])
        operand2 = int(string[1])

        print("string: "+str(string))
        print("operand1:"+str(operand1))
        print("operand2:"+str(operand2))

        if ('+') in query.lower():
            answer = Sum(operand1,operand2)
            speak("Answer is :"+str(answer))
       
        elif ('x') in query.lower():
            answer = multiply(operand1,operand2)
            speak("Answer is :"+str(answer))

        elif ('/') in query.lower():
            answer = divide(operand1,operand2)
            speak("Answer is :"+str(answer))

        elif ('-') in query.lower():
            answer = subtract(operand1,operand2)
            speak("Answer is :"+str(answer))

        elif ('power') in query.lower():
            answer = power(operand1,operand2)
            speak("Answer is :"+str(answer))
        else:
            speak("This is so hard for me, Im sorry")

        break

    else:
        speak("Im not sure I understand")
        speak("Say it again")
        query= takeCommand()
  
'''