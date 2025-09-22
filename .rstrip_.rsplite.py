#Autor: Daniel Salcedo
# Clase de carárcteres 
# \n salto de linea 
# \t tabular
# \" comillas 


#METODOS 
'''
var = "DATO"

print(var.lower())

'''
'''
var = "nombre"
while(True):
    var2 = input("Ingrese la contrseña:\n")
    if (var == var2):
        print("Encontraste el mensaje oculto!")
        break
    else: 
        print("Contraseña incorrecta")
'''
        #Tarea: Para el Lunes
        # .rstrip .rsplite---> ,is metodos


#Para .rstrip():

var = input("Escriba una palabra con o sin espacios: ")
cut = input("Escriba la parte de su palabra que quiere cortar de derecha a izquierda: ")
print(f"Su palabra original es: {var}")

varn = var.rstrip(cut) # en el parametro puede incluir también recortes de palabras que no quiera cortando de derecha a izquierda
print(f"Esta es su nueva palabra {varn}")
if (var != varn):
    print(f"Las variables {var} y {varn} son distintas") 
else: 
    print(f"Las variables {var} y {varn} son iguales.")

#a partir de extraccion de caracteres.
# hacer los problemas pag40. 


#Para rsplit:

var2 = input("coloque una lista de cosas separadas por comas que le gusten: ") #"Extrae" y dide cadenas de texto mediente un parametro que indica donde cortar la cadena y otra en cuantas partes.

print(var2.rsplit(",",len(var2))) # Se usa la función "len" que devuelve un entero que va a hacer como parametro divisorio en la cadena de texto, de esa manera el usuario puede colocar cuantas cosas quiera en su cadena.

