"""Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
parte de una palabra ingresada. ¿Como podemos simplificarlo?"""
cadena = input('Ingresa la clave (debe tener menos de 10 caracteres y no contener @ ni !)')
if len(cadena) > 10:
    print('Ingresaste mas de 10 caracteres')
elif "@" in cadena or "!" in cadena:
    print('Ingresaste simbolos no permitidos')
else:
    print('Ingreso OK')