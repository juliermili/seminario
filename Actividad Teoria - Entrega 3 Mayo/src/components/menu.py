import PySimpleGUI as sg
from src.windows import menu
from src.components import data1

def start():
    window = loop()
    window.close()

def loop():
    window = menu.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-EXIT-"):
            break

        if event == "-DATA1-":
            window.hide()
            data1.start()
            window.un_hide()

    return window