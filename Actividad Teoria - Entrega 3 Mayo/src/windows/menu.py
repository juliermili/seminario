import PySimpleGUI as sg

def build():

    layout = [
        [sg.Button('Data1', size=(50, 2), key="-DATA1-")],
        [sg.Button('Data2', size=(50, 2), key="-DATA2-")],
        [sg.Button('Salir', size=(50, 2), key="-EXIT-")]
    ]

    menu = sg.Window('menu').Layout(layout)
    return menu