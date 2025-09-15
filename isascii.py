# En este codigo se explicara el uso de el metodo isascii en python
# El metodo isascii nos devuelve un booleano, por lo que se evalua si es verdadero o falso y se escribe un mensaje de acuerdo a lo anterior 
# Definimos unas variables con diferentes caracteres
# Ejemplo 1: Todos los caracteres son ASCII
texto1 = "Hola, Python!"
print(texto1.isascii())  # Salida: True
if texto1.isascii() == True:
    print(texto1,": Los caracteres de este parrafo hacen parte del codigo ascii")
else:
    print(texto1, ": Esto no hace parte del codigo ascii")
# Ejemplo 2: Contiene caracteres no ASCII
texto2 = ": ¡Hola, mundo! 😊"
print(texto2.isascii())  # Salida: False
if texto2.isascii() == True:
    print(texto1,": Los caracteres de este parrafo hacen parte del codigo ascii")
else:
    print(texto2, ": Esto no hace parte del codigo ascii")

# Ejemplo 3: Cadena vacía
texto3 = ""
print(texto3.isascii())  # Salida: True (una cadena vacía no tiene caracteres no ASCII)
if texto3.isascii() == True:
    print(texto1,": Los caracteres de este parrafo hacen parte del codigo ascii")
else:
    print(texto3,": Esto no hace parte del codigo ascii")

