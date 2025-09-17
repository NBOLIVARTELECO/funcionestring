# En este codigo se explicara el metodo isalpha
# Este metodo evalua si el contenido de la cadena de caracteres contiene solo letras si es asi devuelve true, si no false
# Ejemplo 1: Todos los caracteres son solo letras
texto1 = "HolaPython"
print(texto1.isalpha())  # Salida: True
if texto1.isalpha() == True:
    print(texto1,": Los caracteres de este parrafo son solo letras")
else:
    print(texto1, ": Este parrafo contiene caracteres que no son letras")
# Ejemplo 2: Contiene caracteres que no son letras
texto2 = ": ¡Hola, Python 1942"
print(texto2.isalpha())  # Salida: False
if texto2.isalpha() == True:
    print(texto1,": Los caracteres de este parrafo son solo letras")
else:
    print(texto2, ": Este parrafo contiene caracteres que no son letras")

# Ejemplo 3: Cadena vacía
texto3 = ""
print(texto3.isalpha())  # Salida: False
if texto3.isalpha() == True:
    print(texto1,": Los caracteres de este parrafo son solo letras")
else:
    print(texto3,": Esta cadena de caracteres vacia devuelve un false con este metodo")
