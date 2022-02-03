from tkinter import *
import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from time import sleep

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

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        var.set("Good Morning Sir")
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 17:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("I am your Voice assistant! How may I help you sir") #Give a name to your assistant

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
    var1.set(query)
    window.update()
    return query

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

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Sir what can i do for you')
            window.update()
            speak("Hello Sir what can i do for you")

        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'current time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'today date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate)

        elif 'thank you' in query:
            var.set("My pleasure sir")
            window.update()
            speak("My pleasure sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform')

        elif 'old are you' in query:
            var.set("I am a little baby only 1 yr")
            window.update()
            speak("I am a little baby only 1 yr")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = """C:\\Users\\Public\\Desktop\\VLC media player""" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Jarvis your voice assistant")
            window.update()
            speak('myself Jarvis your voice assistant')

        elif 'who creates you' in query:
            var.set('My Creator is Ujjwal Saini')
            window.update()
            speak('My Creator is Ujjwal Saini')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Jarvis Your Voice Assistant')
            window.update()
            speak('Hello Everyone! My self Jarvis Your Voice Assistant')

        elif 'open pycharm' in query:
            var.set("Openong Pycharm")
            window.update()
            speak("Opening Pycharm")
            path = "C:\\Users\\Public\\Desktop\\PyCharm Community Edition 2020.3.3 x64" #Enter the correct Path according to your system
            os.startfile(path)

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Users\\Public\\Desktop\\Google Chrome" #Enter the correct Path according to your system
            os.startfile(path)

        elif "open python" in query:
            var.set("Opening Python Ide")
            window.update()
            speak('opening python Ide')
            os.startfile('C:\\Users\\Us\\Desktop\\IDLE (Python 3.8 64-bit)') #Enter the correct Path according to your system

        elif "play" in query:
            var.set("Opening Song In Youtube")
            window.update()
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "open my github account" in query:
            var.set("Opening Your Git Hub Account")
            window.update()
            speak("Opening Your Git Hub Account")
            webbrowser.open("https://github.com/UjjwalSaini07")

        elif "in browser" in query:
            var.set("Opening Your Command in Browser")
            window.update()
            speak("please wait i am searching in browser your command")
            edit_command = query.replace("in browser","")
            webbrowser.open(edit_command)

        elif "ujjwal" in query:
            var.set("WELCOME UJJWAL SIR !!")
            window.update()
            speak("What can i do for you sir !!!")

        elif "my name is" in query:
            var.set(query)
            window.update()
            name_query = query.replace("my name is","")
            print(name_query)
            speak(name_query+" what can i do for you")

        elif ("wait" in query) or ("stop" in query):
            var.set("I AM WAITING FOR 1 MIN")
            window.update()
            speak("I AM WAITING FOR 1 MINUTE AND THAN EXECUTE THE PROGRAM AGAIN")
            for i in range(600):
                sleep(0.10000)
            speak("I AM LISTENING PLEASE GIVE COMMAND")
            var.set("I AM LISTENING PLEASE GIVE COMMAND")
            window.update()

        elif "your hobby" in query:
            var.set("My Hobby Is to Help Everyone")
            window.update()
            speak("My Hobby Is to Help Everyone")

        elif "w3school" in query:
            var.set("OPENING W3SCHOOL IN BROWSER")
            window.update()
            speak("OPENING W3SCHOOL IN BROWSER")
            webbrowser.open("https://www.w3schools.com/")

        elif "voot" in query:
            var.set("OPENING VOOT IN BROWSER")
            window.update()
            speak("OPENING VOOT IN BROWSER")
            webbrowser.open("https://www.voot.com/")

        elif "airtel extreme" in query:
            var.set("OPENING AIRTEL EXTREME IN BROWSER")
            window.update()
            speak("OPENING AIRTEL EXTREME IN BROWSER")
            webbrowser.open("https://www.airtelxstream.in/")

        elif "whatsapp" in query:
            var.set("OPENING WHATSAPP IN BROWSER")
            window.update()
            speak("OPENING WHATSAPP IN BROWSER")
            webbrowser.open("https://web.whatsapp.com/")

        elif "twitter" in query:
            var.set("OPENING TWITTER IN BROWSER")
            window.update()
            speak("OPENING TWITTER IN BROWSER")
            webbrowser.open("https://twitter.com/home?lang=en")

        elif "open gmail" in query:
            var.set("OPENING GMAIL IN BROWSER")
            window.update()
            speak("OPENING GMAIL IN BROWSER")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        else:
            for i in range(100):
                sleep(0.11)
            speak("I NOT UNDERSTAND YOUR COMMAND PLEASE REPEAT AGAIN SLOWLY")

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

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
