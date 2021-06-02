import wolframalpha
import wikipedia
client = wolframalpha.Client("T33TYX-RH989AU2WG")




import PySimpleGUI as sg

sg.theme('LightBlue')
layout = [  [sg.Text("Search")],    
            [sg.Input()],
            [sg.Button('Ok'), sg.Button('Quit')] ]


window = sg.Window('JarSearch', layout)      
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    res = client.query(values[0])
    try:
        wolfram_res = (next(res.results).text)
        sg.popup(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        sg.popup(wiki_res)

window.close()                      