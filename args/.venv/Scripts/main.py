
def suma(*args): # args es igual a una tupla xd y se puede cambiar el nombre jaja
    suma = 0
    cosas = list(args)
    cosas [0] = 5
    for i in cosas:
        suma += i
    return suma

print(suma(1,5, 3, 9 ,2))