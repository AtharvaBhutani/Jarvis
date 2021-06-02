import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss")
    
    elif hour>=12 and hour<=18:
         speak("Good Afternoon Boss")

    else:
         speak("Good Evening Boss")

    speak("How may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        #audio = r.listen(source)

        try:
            print("Recognizing...")
            #query = r.recognize_google(audio, language='en-in')
            print("User said: {query}\n")       

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        #return query
     


_name_ = "_main_"

if _name_ == "_main_":
    wishMe()
    takeCommand()