nombre = "Emanuel Coletti"
primer_nombre = nombre[0:7] #el caracter l solo aparece porque se agrego el 7 ya que esta excluido y no incluido
# primer_nombre = nombre[:7] manera mas corta en teoria
apellido = nombre [8:16]
# apellido = nombre [8:] se imprime hasta el final de la cadena ya que python asume eso
nombre_dos = nombre[0:16:3] # imprimir segun el salto de indice
# nombre_dos = nombre[::2] # imprimir segun el salto de indice asumido por python
nombre_invertido = nombre[::-1] # imprime la cadena de texto de manera invertida

website = "http://www.google.com"

slice = slice(11,-4,1)

sitio = website[slice]

print(site)