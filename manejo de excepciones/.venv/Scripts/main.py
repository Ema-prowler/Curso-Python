
try:
    numerador = int(input("Ingrese un numero: "))
    denominador = int(input("Ingrese un numero: "))
    resultado = numerador / denominador
except ZeroDivisionError as e: # se muestra el mensaje de error
    print(e)
    print("No se puede dividir por cero")
except ValueError: # no se muestra el mensaje de error
    print("por favor ingrese solo numeros")
else:
    print(resultado)
finally:
    print("Fin") #se ejecuta siempre