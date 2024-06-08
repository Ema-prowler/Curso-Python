#Un diccionario es una coleccion no ordenada modificable de pares unicos y valor
capitales = {
    "EE.UU": "Washington D.C",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago de Chile",
    "Brasil": "Brasilia",
    "cursos": ["Python", "C++"],
    "Años": 22
}

capitales.update({"Alemania": "Berlin"})
capitales.pop("EE.UU") #Elimina una clave y su valor del diccionario
#capitales.clear() #Limpia o borra todo el diccionario (Claves y sus Valores)

print(capitales["Chile"]) #metodo comun
print(capitales.get("congo")) #metodo con get que muestra none si el valor no existe en el diccionario
print(capitales.get("Argentina"))
print(capitales.keys()) #para imprimir solo las claves
print(capitales.values()) #para imprimir los valores de las claves
print(capitales.items()) #Imprime el diciconario completo valores y claves.

for key,value in capitales.items():
    print(key,value)