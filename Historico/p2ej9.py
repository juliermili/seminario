"""Practica 2 - Ejercicio 9"""

frase = input('Ingrese una palabra o frase:').lower()
heterograma = True

for letra in frase:
    if heterograma and letra.isalpha() and frase.count(letra)>1:
        heterograma = False
        break

if heterograma: print(f'\'{frase}\' es un heterograma') 
else: print(f'\'{frase}\' NO es un heterograma')