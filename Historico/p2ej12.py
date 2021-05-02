"""Practica 2 - Ejercicio 12
La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
la siguiente:

Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo
anterior, sería:
[
'1*3*1',
'12*32',
'1212*',
'*1011',
]
Nota: Defina al menos una función en el código (si hay mas mejor) y documente las mismas con
docstring que es lo que hacen."""

mapa = [
'-*-*-',
'--*--',
'----*',
'*----',
]

conteo = [
"",
"",
"",
"",
]

def generar_conteo(mapa, conteo):
    """Esta funcion recibe el mapa de minas y devuelve una estructura con el conteo de las minas circundantes a cada espacio"""


linea_conteo = ""
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        linea_conteo = ""
        if  mapa[i][j]== '*':
            conteo[i] += '*'
        else:
            if j != 0:
                linea_conteo += mapa[i][j-1]
            if j != len(mapa[i])-1:
                linea_conteo += mapa[i][j+1]
            if i != 0:
                linea_conteo += mapa[i-1][j]
            if i != len(mapa)-1:
                linea_conteo += mapa[i+1][j]
            conteo[i] += str(linea_conteo.count('*'))
            
print(conteo)


