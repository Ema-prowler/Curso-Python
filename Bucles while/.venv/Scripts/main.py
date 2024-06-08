
nombre = ""


while not nombre or len(nombre) == 0:
#while len(nombre) == 0: otra manera de comprobar si la variable nombre esta vacia
    nombre = input("Ingrese su nombre: ")

print ("Hola " + nombre)