#por defecto la entradas son string , se debe cambiar tipo de dato para el tipo de dato en concreto.
nombre = input("Cual es tu nombre: ? ")
edad = int(input("Cuantos años tienes: ? "))
altura = float(input("Que tan alto eres: ? "))

edad = edad + 1

print("Hola " + nombre)
print("Tienes " + str(edad) + " años")
print("Mides " + str(altura) + " CM")