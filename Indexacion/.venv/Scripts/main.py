
nombre = "emanuel Coletti?"

#if nombre [0].islower(): # comprobacion de si la primera letra esta en minuscula
#    nombre = nombre.capitalize() # transformacion de la letra en minuscula a mayuscula

primer_nombre = nombre[:7].upper() # si el indice es 0 puedes omitir el valor 0 en el indice
appellido = nombre[8:].lower() # transforma todas las letras desde el indice 8 en adelante a minuscula
ultimo_caracter = nombre[-1] #muestra el ultimo caracter de la cadena usando el indice negativo


print(primer_nombre)
print(appellido)
print(ultimo_caracter)
#print(nombre)