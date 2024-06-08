
def saludo(primer_nombre,apellido, edad):
    print("Hola " + primer_nombre + " " + apellido)
    print("Tienes " + str(edad) + " Años")
    print("que tengas un buen dia")

nombre = input("Ingrese su nombre: ")

saludo(nombre, "Coletti", 27)