
import os
import shutil

path = ('folder')

try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print(path + ' No fue encontrado')
except PermissionError:
    print(' No tiene permisos para eliminar la carpeta: ' + path)
except OSError:
    print(' No se puede eliminar la carpeta: ' + path + ' usando esa funcion ')
else:
    print(path + ' Fue eliminado')