import PySimpleGUI as sg

def build():

    layout = [
        [sg.Text('Selecciona el año de registro'), sg.Combo(['2017','2018','2019','2020'], key='YEAR')],
        [sg.Button('Generar', size=(50, 2), key="-DATA1-"),sg.Button('Salir', size=(50, 2), key="-EXIT-")]
    ]

    data1 = sg.Window('data1').Layout(layout)
    return data1