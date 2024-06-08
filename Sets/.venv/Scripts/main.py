utensilios = {"tenedor" , "cuchara" , "cuchillo"} # no imprime elementos duplicados
platos = {"plato" , "bol" , "taza", "cuchara"}

#utensilios.add("cucharita") #agregar elemento
#utensilios.remove("cuchara") # quita un elemento
#utensilios.pop() # quita un elemento aleatorio del Set
#utensilios.clear() #borra todos los elementos

#utensilios.update(platos) #Actualiza el set y/o agrega mas elementos deseados

print(utensilios.difference(platos)) #muestra todos los valores sin los repetidos
print(utensilios.intersection(platos))# muestra unicamente todos los valores repetidos

for x in utensilios:
    print(x)
