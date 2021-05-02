def completa_curso_de_10(*args, cantidad):
	resp = input('Desea completar el curso? (S/N)  ')
	if resp.upper() == 'S':
		for cant in range (cantidad):
			nombre = input('Ingresa nombre de nuevo integrante')
			args = args + (nombre,)
	return args
 
curso1 = completa_curso_de_10('Juan','Ana','Rocío','Estela', 6)
curso2 = completa_curso_de_10 ('Pablo', 'Pedro', 8)
 
print (f'El curso1 actualizado es: {curso1}')
print (f'El curso2 actualizado es: {curso2}')
