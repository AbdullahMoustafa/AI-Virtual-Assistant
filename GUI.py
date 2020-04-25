import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import smtplib 
from gtts import gTTS
import pyttsx3 
from pyttsx3 import voice
import requests
from pprint import pprint
import re
import math
from tkinter import * 
from draw import drawStart
from game import startGame
import tkinter as tk
from translate import toFrench,toGerman,toSpanish,toItalian,toPortuguese
from googlesearch import search 
from calculator import Sum,multiply,subtract,divide,power,sin,cos,tan
# import cv2


pos = N

print("Imported")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #1/0 for female/male
engine.setProperty('rate',150)
engine.setProperty('volume',2)

def speakforeigner(text):
    voice = engine.getProperty('voices')[0] # the foreigner voice
    engine.setProperty('voice', voice.id)
    engine.say(text)
    engine.runAndWait()

def googleSearch(text_to_search):
    query = text_to_search
    for a in search(query, tld="com", lang='en', num=10, start=0, stop=1, pause=2):
        None
    for b in search(query, tld="com", lang='en', num=10, start=1, stop=1, pause=2):
        None
    for c in search(query, tld="com", lang='en', num=10, start=2, stop=2, pause=2):
        None
    links = (str(a)+"\n"+str(b)+"\n"+str(c))
    return links

def time():
    hours = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute
    if(hours <= 12):
        time= str(hours)+str("&")+str(minutes)+str("minutes ")+str(" a m")
    else:
        time= str(hours)+str("&")+str(minutes)+str("minutes")+str(" p m")
    # print(time)
    return time
timevalue=time()
def date():
    from datetime import date
    today = date.today()
    day_name = date.today().strftime("%A")
    dateToday = today.strftime("%B %d, %Y")
    date_value = str(day_name)+" "+str(dateToday)
    # print("date =", date)
    return date_value
datevalue = date()
def temperture():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Alexandria&APPID=ab4c2af67b34f964a01732a7f12e0f95')
    #pprint(r.json())
    return r.json()
tempvalue = temperture()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning "+ USER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon" + USER)
    speak("How can I help you?")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abdullahmoustafa03@gmail.com', 'pass')
    server.sendmail('abdullahmoustafa03@gmail.com',to, content )
    server.close()

def speak(text):
    engine.say(text)
    engine.runAndWait()
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

def InsertText(text):
    output.delete('1.0',END)
    output.insert(tk.INSERT,text)

def click():                   #once click on NAME button
    entered_text = textentry.get()   #stored data in text box
    definition = "Hello " +str(entered_text)+ " I'm Genia your virtual assistant\npress ASK to ask for anything"
    output.insert(END,definition)

    # output.insert(END,definition)
    speak(definition)
    nameButton = Button(window, text= "Enter your Name", width = 20, command = click, fg = "#272324", bg= "#A9A9A9",state="disabled").grid(row=3, column=0 ,sticky=pos)
def refresh():                   #once click on ASK button
    definition = "I'm listening.."
    InsertText(definition)

    speak(definition)
    main()

def main():
    import tkinter as tk

    query = takeCommand()

    while(query != None):


        if ('answer of'  in query.lower() or  'calculate' in query.lower() or  '/' in query.lower()  or  'x' in query.lower()  or  '-' in query.lower()  or  '+' in query.lower()  or  'tan' in query.lower()  or  'sine' in query.lower()  or  'cosine' in query.lower() or  'power' in query.lower()):
            speak("Working on it...")
            string = query
            #calculate 10 + 10 
            string = re.findall('\d+', string)

            if (len(string) < 2):
                
                operand1 = int(string[0])
                # print(operand1)
                
                if 'sine'  in query.lower():
                    answer = sin(operand1)
                    speak("Answer is :"+str(answer))
                    InsertText("Answer is : "+ str(answer))
                elif 'cosine' in query.lower():
                    answer = cos(operand1)
                    speak("Answer is :"+str(answer))
                    InsertText("Answer is : "+ str(answer))
                elif 'tan'  in query.lower():
                    answer = tan(operand1)
                    speak("Answer is :"+str(answer))
                    InsertText("Answer is : "+ str(answer))
            else:
                operand1 = int(string[0])
                operand2 = int(string[1])
   
            # print("string: "+str(string))
            # print("operand1:"+str(operand1))
            # print("operand2:"+str(operand2))

                if ('+') in query.lower():
                    answer = Sum(operand1,operand2)
                    speak("Answer is :"+str(answer))
                    InsertText("Answer is : "+ str(answer))
            
                elif ('x') in query.lower():
                    answer = multiply(operand1,operand2)
                    speak("Answer is :"+str(answer))
                    output.delete('1.0',END)
                    InsertText("Answer is : "+ str(answer))


                elif ('/') in query.lower():
                    answer = divide(operand1,operand2)
                    speak("Answer is :"+str(answer))
                    InsertText("Answer is : "+ str(answer))


                elif ('-') in query.lower():
                    answer = subtract(operand1,operand2)
                    if int(answer) <0:
                        speak("Answer is negtive:"+str(answer))
                    else:
                        speak("Answer is : "+str(answer))                    
        
                    InsertText("Answer is : "+ str(answer))


                elif ('power') in query.lower():
                    answer = power(operand1,operand2)
                    speak("Answer is :"+str(answer))
                    InsertText("Answer is : "+ str(answer))

                else:
                    speak("This is so hard for me, Im sorry")
                    InsertText("This is so hard for me, Im sorry")


            break

        if ('wikipedia') in query.lower():
            speak('searching on wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            # print(results)
            if results == False:
                speak("I didnt find any information")
                InsertText("I didnt find any information")
            else:
                print(results)
                InsertText(results)
                speak(results)
                
            break

        if ('search on google for' in query.lower()  or 'google for' in query.lower() or 'search for' in query.lower()):
            text = query
            text = text.replace('google','')
            text = text.replace('search on' or 'search for' or 'search about','')
            speak("Searching on google..")
            # InsertText("Searching on google..")
            
            links = googleSearch(text)
            speak('I found this links may it could help you...')
            # print(links)
            InsertText(links)                
            break

        if (('translate' in query.lower()) or ('french' in query.lower())  or ('spanish' in query.lower())  or ('german' in query.lower())  or ('italian' in query.lower())  ):
            if ('french') in query.lower():
                ret = toFrench(query)
                print(ret)
                speakforeigner(ret)
                InsertText(ret)
                voice = engine.getProperty('voices')[1] 
                engine.setProperty('voice', voice.id)

            elif ('german') in query.lower():
                ret = toGerman(query)
                print(ret)
                speakforeigner(ret)
                InsertText(ret)
                voice = engine.getProperty('voices')[1]
                engine.setProperty('voice', voice.id)
            
            elif ('spanish') in query.lower():
                ret = toSpanish(query)
                print(ret)
                speakforeigner(ret)
                InsertText(ret)
                voice = engine.getProperty('voices')[1]
                engine.setProperty('voice', voice.id)

            elif ('italian') in query.lower():
                ret = toItalian(query)
                print(ret)
                speakforeigner(ret)
                InsertText(ret)
                voice = engine.getProperty('voices')[1]
                engine.setProperty('voice', voice.id)

            elif ('portuguese') in query.lower():
                ret = toPortuguese(query)
                print(ret)
                speakforeigner(ret)
                InsertText(ret)
                voice = engine.getProperty('voices')[1]
                engine.setProperty('voice', voice.id)
                
            else:
                speakforeigner("Im sorry I dont understand this language")
                InsertText("Im sorry I dont understand this language")

            break

        if ('open youtube') in query.lower():
            url = "youtube.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            speak("hold on")
            webbrowser.get(chrome_path).open(url)
            break
 
        if ('open google'  in query.lower()   or 'google' in query.lower()) :
            url = "google.com"
            speak("Im wondering what are you looking for")
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
            break

        if 'open facebook' in query.lower():
            url = "facebook.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            speak("Im on it")
            webbrowser.get(chrome_path).open(url)
            break

        if 'open linkedin' in query.lower():
            url = "linkedin.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            speak("lets get professional")
            webbrowser.get(chrome_path).open(url)
            break

        if 'open stackover flow' in query.lower():
            url = "stackoverflow.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            speak("hold on")
            webbrowser.get(chrome_path).open(url)
            break

        if 'open soundcloud' in query.lower():
            url = "soundcloud.com"
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            speak("Im on it")
            webbrowser.get(chrome_path).open(url)
            break

        if ('play music' or 'play my list' or 'open my playlist' or 'open my favorite songs')in query.lower():
            songs_dir = 'E:\\desktop\\FUN\\Myplaylist' 
            songs = os.listdir(songs_dir)
            speak("playlist shuffle..")
            InsertText('playlist shuffle..')
            
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            break

        if ('the time now' in query.lower() or 'time' in query.lower() or 'what time is it' in query.lower() or 'how much oclock' in query.lower()):
            time = timevalue
            speak("The time is")
            speak(time)
            InsertText(time)
            

            break

        if ('what is the date' in query.lower() or 'What date is it' in query.lower() or 'What day is it' in query.lower() or "today's date" in query.lower()):
            date = datevalue
            speak("Today is ")
            speak(date)
            InsertText(date)
            break

        if ('what is the temperature now' or 'What is the weather today' or 'is it hot today' or "is it cold today") in query.lower():
            temp = tempvalue
            speak("Today's temperture is ")
            speak(temp)
            InsertText(temp)
            break

        if ('open my code' or 'open code' or 'your code') in query.lower():
            code_dir = 'C:\\Users\\Abdullah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe' 
            os.startfile(os.path.join(code_dir))
            break

        if ('f*** you' or 'motherfucker' or 'you are disgusting'  or 'ugly' or 'bitch' or 'you are stupid' or "you're stupid") in query.lower():
            speak('You are so rude, I will not respond to that')
            InsertText('You are so rude, I will not respond to that')
            break

        if ('love you' in query.lower() or 'would you marry me' in query.lower()):
            speak('oh, you are so sweet')
            InsertText('oh, you are so sweet')
            break

        if 'email to tina' in query.lower():
            try:
                speak("what should I send")
                content = takeCommand()
                to ='yousteena95@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent successfully")
                break
            except Exception as e:
                print(e)
                speak("There is a problem in email security, please check it and try again")
                break

        if ('draw' in query.lower() or 'drew' in query.lower()):
            speak("Lets draw, to save you drawing just press control  S")
            InsertText('press " CTRL+S" to save your draw..')
            drawStart()
            
            break

        if ('game' in query.lower()):
            speak("lets play a game")
            InsertText("Have fun..")
            startGame()

            
            break
    
        else:
            speak("Im not sure I understand")
            speak("Say it again")
            InsertText("Im not sure I understand\nSay it again")
            query= takeCommand()


def close_window():
    window.destroy()
    exit()

#Make the window
window = Tk()
window.title("GENIA")
window.iconbitmap('C:\\Users\\Abdullah\\Desktop\\AI virtual Assistance\\Genio\\brain_sWy_icon.ico')
window.configure(background = 'black')
window.geometry('595x660')

#Photo Label
AssisstancePhoto = 'C:\\Users\\Abdullah\\Desktop\\AI virtual Assistance\\Genio\\robot.png'
photo1 = PhotoImage(file=AssisstancePhoto)
Label (window , image = photo1, bg ='black') .grid(row=0, column = 0, sticky=E)

# #Text Label

#create a text entry box
textentry = Entry(window, width = 50 ,bg="grey")
textentry.grid(row =2 , column=0, sticky =pos)
# text = textentry.get()

#Add a submit button 
nameButton = Button(window, text= "Enter your Name", width = 20, command = click, fg = "#272324", bg= "#A9A9A9").grid(row=3, column=0 ,sticky=pos)
askButton = Button(window, text= "ASK", width= 20, command = refresh, fg = "#272324", bg= "#A9A9A9").grid(row=4, column= 0 , sticky=pos)

#textbox
output = Text(window, width=68 , height = 5, wrap = WORD, bg= 'black',fg = "#00D1FF")
output.grid(row=5, column=0, columnspan=2, sticky=pos)
output.config(state=NORMAL)

#Exit Text Label
# Label (window,text="Click to Exit", bg= 'black',fg = "white",font = "none 10 bold" ).grid (row=6 ,column =0, sticky=W)
#Exit Button
Button(window, text= "EXIT", width= 14, command=close_window, fg = "#272324", bg= "#A9A9A9").grid(row=7, column= 0 , sticky=pos)

Label (window,text="© GENIA is an AI virtual Assistance developed to you by Abdullah Moustafa", bg= 'black',fg = "white",font = "none 7 bold" ).grid (row=8 ,column =0, sticky=S)

window.mainloop()




'''
Another game
NLP
Open videos and images 

'''