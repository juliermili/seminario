def completa_curso_de_10(args, cantidad):
	resp = input('Desea completar el curso? (S/N)  ')
	if resp.upper() == 'S':
		for cant in range (cantidad):
			nombre = input('Ingresa nombre de nuevo integrante')
			args.append(nombre)
	return args

lista1 = ['Juan','Ana','Rocío','Estela']
lista2 = ['Pablo', 'Pedro']
curso1 = completa_curso_de_10(lista1, 6)
curso2 = completa_curso_de_10 (lista2, 8)
 
print (f'El curso1 actualizado es: {curso1}y {type(curso1)}')
print (f'El curso2 actualizado es: {curso2}')