import PySimpleGUI as sg

def build():

    layout = [
        [sg.Text('Analizar registro de ranking mundial de universidad y generar archivo con las 10 universidades con mas pocentaje de alumnos internacionales')],
        [sg.Button('Generar', size=(50, 2), key="-DATA2-"),sg.Button('Salir', size=(50, 2), key="-EXIT-")]
    ]

    data2 = sg.Window('data2').Layout(layout)
    return data2