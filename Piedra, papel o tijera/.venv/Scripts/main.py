import random

lista = ['piedra', 'papel', 'tijera']

while True:
    computadora = random.choice(lista)

    jugador = None

    while jugador not in lista:
        jugador = input('piedra, papel o tijera: ').lower()

    if jugador == computadora:
        print('Computadora', computadora)
        print('Jugador', jugador)
        print('Empate')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Computadora', computadora)
            print('Jugador', jugador)
            print('perdiste')
        if computadora == 'tijera':
            print('Computadora', computadora)
            print('Jugador', jugador)
            print('ganaste')
    elif jugador == 'papel':
        if computadora == 'tijera':
            print('Computadora', computadora)
            print('Jugador', jugador)
            print('perdiste')
        if computadora == 'piedra':
            print('Computadora', computadora)
            print('Jugador', jugador)
            print('ganaste')
    elif jugador == 'tijera':
        if computadora == 'piedra':
            print('Computadora', computadora)
            print('Jugador', jugador)
            print('perdiste')
        if computadora == 'papel':
            print('Computadora', computadora)
            print('Jugador', jugador)
            print('ganaste')
    jugar_de_nuevo = input('¿Desea jugar de nuevo? (S/N): ').lower()

    if jugar_de_nuevo != 's':
        break
print('adios')