
#nombre = "SHRUT" Variable GLOBAL

def mostrar_nombre():
    nombre = "ema"
    print(nombre) #la variable que se imprime solo existe en la funcion por lo tanto no se puede invocar desde afuera

mostrar_nombre()
#print(nombre) esto no funcionara

#python sigue esta nomenclatura
#  primero se dirige a las variables locales
#  luego se dirige a las variables cercanas
#  sigue con las variables globales
#  y por ultimo las variables integradas
#
