
def hola(**kwargs):# kwargs es un parametro que empaqueta una cantidad variable clave en un diccionario

    #print('Hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'] + ' ' + kwargs['segundo_nombre'])
    print('hola', end=' ')
    for clave, valor in kwargs.items():
        print(valor, end=' ')
hola(titulo = 'señor', nombre='Emanuel', apellido='Coletti', segundo_nombre='python')