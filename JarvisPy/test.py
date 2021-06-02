import wolframalpha
import wikipedia
import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
import PySimpleGUI as sg
import pyttsx3

layout = [  [sg.Text('Welcome Back Sir')],
            [sg.Text('How can I be of assistance'), sg.InputText()],
            [sg.ReadButton('Speak'), sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Jarvis', layout)
engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    # print(event, values)
    if event == 'Speak':
        with m as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            value = r.recognize_google(audio, language='en-US')
            print(value)
            window[0].update(value)
            window.write_event_value('Ok', '')
    elif event == 'Ok':
        if values[0] == '':
            continue
    try:
        wolfram_res = (next(res.results).text)
        sg.popup(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        sg.popup(wiki_res)

        engine.runAndWait()

window.close()