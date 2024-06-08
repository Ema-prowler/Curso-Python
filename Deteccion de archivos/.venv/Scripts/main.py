
import os

path = 'H:\\Complementos\\Escritorio\\Test.txt'

if os.path.exists(path):
    print('la ubicacion existe')
    if os.path.isfile(path): # se verifica si es un archivo pero no si es un directorio/carpeta
        print('es un archivo')
    elif os.path.isdir(path): # se verifica si es un directorio
        print('es un directorio')
else:
    print('la ubicacion no existe')