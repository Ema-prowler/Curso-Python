temperatura = int(input("Cual es la temperatura afuera:? "))

if temperatura >= 0 and temperatura <= 30:
    print("La temperatura esta bien hoy :D")
elif temperatura <0 or temperatura > 30:
    print("La temperatura esta mal hoy :(")
#se puede usar tambien el operador not