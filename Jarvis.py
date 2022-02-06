import time
from tkinter import *
import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import ctypes
from time import sleep
import numpy as np
from PIL import Image
import cv2
import pyautogui
import calendar
from time import strftime
import speedtest
import pyspeedtest
from tkinter import messagebox
import tkinter.ttk as ttk


# Import Our Own Creating Library

import Calendar_GUI
import Clock_GUI
import Speedtest_by_Tkinter
import Stopwatch
import Turtle_Clock
# import Screen_Recorder_Python

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# -------------------------------------------------------------------------------------------------------------
# Wish ME
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        var.set("Good Morning Sir")
        window.update()
        speak("Good Morning Sir!")
    elif hour <= 16:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("I am your Voice Assistant!!") #Give a name to your assistant
    speak("What should i call you sir")
    username = takeCommand()
    speak("Welcome,"+username+".")
    # speak(username)
    speak("Sir What Should I do For You Sir")

# -------------------------------------------------------------------------------------------------------------
#
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
        print("Error")
    var1.set(query)
    window.update()
    return query

# -------------------------------------------------------------------------------------------------------------
# Function Of screenshot
def takeScreenshot():
    speak("taking screenshot, sir")

    # take screenshot using pyautogui
    image = pyautogui.screenshot()
    # since the pyautogui takes as a PIL(pillow) and in RGB we need to convert it to numpy array and BGR
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    # writing it to the disk using opencv
    cv2.imwrite("image1.png", image)
    speak("screenshot taken, sir. Do you want me to open it?")
    image_open = Image.open("image1.png")
    image_open.show()
    speak("Here it is sir. Looks good")
    time.sleep(6)


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()

    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()

        if ('exit' in query) or ('bye' in query):
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            sleep(1)
            speak("Hope you were satisfied by my Services..")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        # -------------------------------------------------------------------------------------------------------------
        # Taking Screenshot
        elif "screenshot" in query:
            takeScreenshot()

        # -------------------------------------------------------------------------------------------------------------
        # Search On Web
        elif 'search' in query:
            # a basic web crawler using selenium
            webbrowser.open(input)
            return

        # -------------------------------------------------------------------------------------------------------------
        # Open Youtube
        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        # -------------------------------------------------------------------------------------------------------------
        # Open Googlg
        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        # -------------------------------------------------------------------------------------------------------------
        # Open Chrome
        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Users\\Public\\Desktop\\Google Chrome" #Enter the correct Path according to your system
            os.startfile(path)

        # -------------------------------------------------------------------------------------------------------------
        # Explain the Article or anything you want
        elif "in browser" in query:
            var.set("Opening Your Command in Browser")
            window.update()
            speak("please wait i am searching in browser your command")
            edit_command = query.replace("in browser","")
            webbrowser.open(edit_command)

        # -------------------------------------------------------------------------------------------------------------
        # Know Current Time
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        # -------------------------------------------------------------------------------------------------------------
        # Locking The Device
        elif ('lock window' in query) or ('locking' in query):
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        # -------------------------------------------------------------------------------------------------------------
        # Know Today Date
        elif ('today date' in query) or ('the date' in query) or ('date today' in query):
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate)

        # -------------------------------------------------------------------------------------------------------------
        # Open VlC
        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = """C:\\Users\\Public\\Desktop\\VLC media player""" #Enter the correct Path according to your system
            os.startfile(path)

        # -------------------------------------------------------------------------------------------------------------
        #Open Github Page
        elif "open my github account" in query:
            var.set("Opening Your Git Hub Account")
            window.update()
            speak("Opening Your Git Hub Account")
            webbrowser.open("https://github.com/UjjwalSaini07")

        # -------------------------------------------------------------------------------------------------------------
        # Open Pycharm
        elif 'open pycharm' in query:
            var.set("Opening Pycharm")
            window.update()
            speak("Opening Pycharm")
            path = "C:\\Users\\Public\\Desktop\\PyCharm Community Edition 2021.1.2 x64" #Enter the correct Path according to your system
            os.startfile(path)

        # -------------------------------------------------------------------------------------------------------------
        # Open Python
        elif "open python" in query:
            var.set("Opening Python Ide")
            window.update()
            speak('opening python Ide')
            os.startfile('C:\\Users\\Us\\Desktop\\IDLE (Python 3.8 64-bit)') #Enter the correct Path according to your system

        # -------------------------------------------------------------------------------------------------------------
        # Play Video In Youtube
        elif "play" in query:
            var.set("Opening Song In Youtube")
            window.update()
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        # -------------------------------------------------------------------------------------------------------------
        # Save Your name in server Database
        elif "my name is" in query:
            var.set(query)
            window.update()
            name_query = query.replace("my name is","")
            print(name_query)
            speak(name_query+" what can i do for you")

        # -------------------------------------------------------------------------------------------------------------
        # Opening Calendar
        elif "calendar" in query:
            speak("Opening Calendar Sir")
            speak("Select Year and Month,To see Your Desire Output")
            Calendar_GUI.date_calendar()
            # break
            exit()
            speak("Sir i wait for 15 second ,you See Calendar then i execute again")
            time.sleep(15)
            speak("Sir I execute again please give me next order")

        # -------------------------------------------------------------------------------------------------------------
        # Opening Clock
        elif "clock" in query:
            speak("Opening Digital Clock Sir")
            Clock_GUI.tkinter_clock()

        # -------------------------------------------------------------------------------------------------------------
        # Opening Clock
        elif "speed test" in query:
            speak("Opening Internet Speedtester Sir")
            Speedtest_by_Tkinter.internet_speedtest()

        # -------------------------------------------------------------------------------------------------------------
        # Opening Clock
        elif "analog clock" in query:
            speak("Opening Analog Clock Sir")
            Turtle_Clock.turtle_clock()

        # -------------------------------------------------------------------------------------------------------------
        # Opening Clock
        elif "stopwatch" in query:
            speak("Opening Stopwatch Sir")
            Stopwatch.stopwatch_tkinter()

        # -------------------------------------------------------------------------------------------------------------
        # Make Note in Notepad
        elif "write a note" in query:
            speak("What should i write, sir")
            speak("Sir i Wait For 5 sec You Think What Should You write in Note then you dectate me and i write in the Notepad")
            time.sleep(6)
            speak("Now Sir Speak What You Want To write in the Note")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        # -------------------------------------------------------------------------------------------------------------
        # Show Above Note
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        # -------------------------------------------------------------------------------------------------------------
        # Jarvis Wait for 1 Min
        elif ("wait" in query) or ("stop" in query):
            var.set("I AM WAITING FOR 1 MIN")
            window.update()
            speak("I Should Wait for 1 Minute Then execute again ")
            time.sleep(60)
            # speak("For How Much Time in Second i Should Wait")
            # waiting_time = int(takeCommand())
            # speak("I am Waiting For")
            # speak(waiting_time)
            # speak("Seconds")
            # time.sleep(waiting_time)
            speak("I AM LISTENING PLEASE GIVE COMMAND")
            var.set("I AM LISTENING PLEASE GIVE COMMAND")
            window.update()

        # -------------------------------------------------------------------------------------------------------------
        # Open  w3school
        elif "open w3school" in query:
            var.set("OPENING W3SCHOOL IN BROWSER")
            window.update()
            speak("OPENING W3SCHOOL IN BROWSER")
            webbrowser.open("https://www.w3schools.com/")

        # -------------------------------------------------------------------------------------------------------------
        # Open Whatsapp
        elif "open whatsapp" in query:
            var.set("OPENING WHATSAPP IN BROWSER")
            window.update()
            speak("OPENING WHATSAPP IN BROWSER")
            webbrowser.open("https://web.whatsapp.com/")

        # -------------------------------------------------------------------------------------------------------------
        # Open Twitter
        elif "open twitter" in query:
            var.set("OPENING TWITTER IN BROWSER")
            window.update()
            speak("OPENING TWITTER IN BROWSER")
            webbrowser.open("https://twitter.com/home?lang=en")

        # -------------------------------------------------------------------------------------------------------------
        # Open Gmail
        elif "open gmail" in query:
            var.set("OPENING GMAIL IN BROWSER")
            window.update()
            speak("OPENING GMAIL IN BROWSER")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        # -------------------------------------------------------------------------------------------------------------
        #Knowing the Hobby of Jarvis
        elif "your hobby" in query:
            var.set("My Hobby Is to Help Everyone")
            window.update()
            speak("My Hobby Is to Help Everyone")

        # -------------------------------------------------------------------------------------------------------------
        elif "ujjwal" in query:
            var.set("WELCOME UJJWAL SIR !!")
            window.update()
            speak("What can i do for you sir !!!")

        # -------------------------------------------------------------------------------------------------------------
        # Knowing The name and intro of jarvis
        elif 'your name' in query:
            var.set("Myself Jarvis your Voice Assistant")
            window.update()
            speak('myself Jarvis your voice assistant')

        # -------------------------------------------------------------------------------------------------------------
        # Knowing Creator of Jarvis
        elif ('who creates you' in query) or ('your Boss' in query) or ('your owner' in query):
            var.set('My Creator is Ujjwal Saini')
            window.update()
            speak('My Creator is Ujjwal Saini')

        # -------------------------------------------------------------------------------------------------------------
        # Say Hello
        elif 'say hello' in query:
            var.set('Hello Everyone! My self Jarvis Your Voice Assistant')
            window.update()
            speak('Hello Everyone! My self Jarvis Your Voice Assistant')

        # -------------------------------------------------------------------------------------------------------------
        # Telling Thank you to him
        elif 'thank you' in query:
            var.set("My pleasure sir")
            window.update()
            speak("My pleasure sir")

        # -------------------------------------------------------------------------------------------------------------
        # Taking his opinion
        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. Tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform')

        # -------------------------------------------------------------------------------------------------------------
        # Knowing Jarvis Age
        elif 'old are you' in query:
            var.set("I am a little baby only 1 yr")
            window.update()
            speak("I am a little baby only 1 yr")

        # -------------------------------------------------------------------------------------------------------------
        # Hello to Jarvis
        elif 'hello' in query:
            var.set('Hello Sir what can i do for you')
            window.update()
            speak("Hello Sir what can i do for you")

        # Execute Else Command where no command Work
        else:
            for i in range(100):
                sleep(0.11)
            speak("I NOT UNDERSTAND YOUR COMMAND PLEASE REPEAT AGAIN SLOWLY")

# -------------------------------------------------------------------------------------------------------------
#
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

# -------------------------------------------------------------------------------------------------------------
#
label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('JARVIS YOUR VOICE ASSISTANT')
window.iconbitmap("Computer_icon.ico")

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()