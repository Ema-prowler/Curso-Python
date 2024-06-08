

str_1 = "leche"
str_2 = "casar"

#print("Arroz con leche me quiero casar") #forma comun
#print("Arroz con " + str_1 + " me quiero " + str_2) #forma concatenada
#print("Arroz con {} me quiero {}".format("leche", "casar")) # forma formateada
#print("Arroz con {} me quiero {}".format(str_1, str_2)) # los {} se interpretan como variables o (campo de formato)
print("Arroz con {1} me quiero {0}".format(str_1, str_2)) # se puede usar el indice de los argumentos
print("Arroz con {0} me quiero {1}".format(str_1, str_2)) # se puede usar el nombre de los argumentos
print("Arroz con {str_2} me quiero {str_1}".format(str_1 = "leche", str_2 = "casar"))
print("Arroz con {str_2} me quiero {str_1}".format(str_1 = str_1, str_2 = str_2))

texto = "arroz con {} me quiero {}"

#print(texto.format(str_1, str_2))


nombre = "Emanuel"
#print("Hola, mi nombre es: {}".format(nombre))
#print("Hola, mi nombre es: {:10}. mucho gusto :D".format(nombre))
#print("Hola, mi nombre es: {:<10}. mucho gusto :D".format(nombre))
#print("Hola, mi nombre es: {:>10}. mucho gusto :D".format(nombre))
#print("Hola, mi nombre es: {:^10}. mucho gusto :D".format(nombre))



numero_1 = 1000
numero = 3.14159
print("El numero PI es: {}".format(numero))
print("El numero PI es: {:.2f}".format(numero))
print("El numero PI es: {:b}".format(numero_1)) #binario
print("El numero PI es: {:o}".format(numero_1)) #octal
print("El numero PI es: {:x}".format(numero_1)) #hexadecimal
print("El numero PI es: {:e}".format(numero_1)) #Notacion cientifica


