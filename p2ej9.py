frase = input('Ingrese una palabra o frase:').lower()
heterograma = True

for letra in frase:
    if heterograma == True and letra.isalpha() and frase.count(letra)>1:
        heterograma = False
        print(letra, letra.isalpha(), frase.count(letra))


print(f'\'{frase}\' es un heterograma: {heterograma}')