import pyttsx3
import datetime
import wolframalpha
client = wolframalpha.Client("T33TYX-RH989AU2WG")

import pyttsx3
import speech_recognition as sr
import datetime
import os
#import wikipedia
import webbrowser
#import pyjokes




engine = pyttsx3.init('sapi5', True)
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    
    elif hour>=12 and hour<=18:
         speak("Good Afternoon Sir")

    else:
         speak("Good Evening Sir")

    speak("and hello by the way")



def takeCommand():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("listening complete")

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")     
            return query
        except Exception as e:
            # print(e)
            print("Say that again please...")
            speak("Say that again please...")
            return "None"

import PySimpleGUI as sg

sg.theme('LightBlue')
layout = [  [sg.Text("Search")],    
            [sg.Input(sr)],
            [sg.Button('Ok'), sg.Button('Quit')] ]


window = sg.Window('Jarvis', layout)      
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    res = client.query(values[0])
    sg.popup(next(res.results).text)

window.close()                      
          
#_name_ = "_main_"

#if _name_ == "_main_":
wishMe()
while True:
    query = takeCommand()
    print(query)

    if "buy" in query:
        speak("Bye sir")
        break

    if "Jarvis" in query:
        speak ("yes sir")

    if "what" in query:
        print("searching...")
        speak("searching Wikipedia...")
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    if "how" in query:
        speak ("couldn't be better")  

    elif "open YouTube" in query:
        webbrowser.open("youtube.com")
    
    elif "open Google" in query:
        webbrowser.open("google.com")

    elif "open Amazon" in query:
        webbrowser.open("Amazon.in")

    elif "open Geeks for Geeks" in query:
        webbrowser.open("geeksforgeeks.com")

    elif "open stack overflow" in query:
        webbrowser.open("stackoverflow.com")

    elif "open pepakura" in query:
        webbrowser.open("pepakura.eu")

    elif "open my nearby" in query:
        webbrowser.open("malwarebytes.com")

    

    elif "open Marble " in query:
        webbrowser.open("marvelcinematicuniverse.fandom.com")

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strTime}")

    elif "open Notepad" in query:
        path = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(path)

    elif "joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif "the hell" in query:
        speak("sir, that's the only thing i got")

    elif "designer" in query:
        speak("working on a new project are we sir?")

    elif "yes" in query:
        path = "C:\\Program Files (x86)\\tamasoftware\\pepakura4en\\designer\\pepakura4.exe"
        os.startfile(path)

    elif "Viewer" in query:
        path = "C:\\Program Files (x86)\\tamasoftware\\pepakura4en\\viewer\\pepakura_viewer4.exe"
        os.startfile(path)
    
    elif "command" in query:
        os.system("start CMD")

    elif "protocol" in query:
        speak("running procedures and getting suit ready")

    elif "I will be" in query:
        speak("Where are you going sir?")

    elif "To the bathroom" in query:
        speak("Ok, sure sir")



