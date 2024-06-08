
try:
    with open('texto.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('No existe el archivo')
print(file.closed)