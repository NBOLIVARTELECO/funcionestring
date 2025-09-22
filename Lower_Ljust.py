print("hola mundo /n "" ")
print("siguiente linea")

var = "nombre" 

print(var,type(var))
print(len(var))

# Autor: Antonio Betancourt
# Ejemplo Metodo de extracción

primera = var[0]          
        
ultima = var[-1]          

print(f"Palabra: {var}\n")

print(f"Primera letra: {primera}\n")

print(f"Última letra: {ultima}\n")


# Ejemplo con lower() y ljust()

texto = "HOLA MUNDO"
print("Texto en mayusculas: ", texto, "\n")

# lower(): convierte todo el texto en minúsculas

texto_en_minusculas = texto.lower()
print("Texto en minúsculas: ", texto_en_minusculas, "\n")

#ljust(): alinea el texto a la izquierda y rellena con un carácter

texto_justificado = texto.ljust(20, "-")
print("Texto justificado a la izquierda: ", texto_justificado, "\n")


"""
while(True):
    var2 = input("ingrese una palabra: ")

    if(var == var2):
        print("Usted descubrio el mensaje oculto")
        break
    else:
        print("palabra equivocada")
    
"""

