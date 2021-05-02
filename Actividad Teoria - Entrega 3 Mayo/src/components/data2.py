import PySimpleGUI as sg
import csv, json
from src.handlers import data2 as data2_handler
from src.windows import data2 as data2_window

def start():
    window = loop()
    window.close()

def loop():
    window = data2_window.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-EXIT-"):
            break

        if event == "-DATA2-":
            data2_handler.start()
            sg.Popup('El archivo json fue generado con el nombre resultados_data2')
            break

    return window