import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

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
            return "None"
          
#_name_ = "_main_"

#if _name_ == "_main_":
wishMe()
while True:
    query = takeCommand()
    print(query)

    if "Wikipedia" in query:
        print("searching...")
        speak("searching Wikipedia...")
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

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
    
    if "thank you" in query:
        speak("always at your service sir")

    
    #break

    