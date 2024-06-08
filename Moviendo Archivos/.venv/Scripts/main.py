
import os

origen = ('folder')
destino = ('D:\\folder')

try:
    if os.path.exists(destino):
        print('El archivo ya existe')
    else:
        os.replace(origen, destino)
        print(origen + ' El archivo fue movido')
except FileNotFoundError:
    print(origen + ' No fue encontrado')

