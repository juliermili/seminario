import PySimpleGUI as sg
import csv, json
from src.handlers import data1 as data1_handler
from src.windows import data1 as data1_window

def start():
    window = loop()
    window.close()

def loop():
    window = data1_window.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-EXIT-"):
            break

        if event == "-DATA1-":
            data1_handler.start(values['YEAR'])
            sg.Popup('El archivo felices.json fue generado')
            break

    return window