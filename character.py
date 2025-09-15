print("hola mundo /n "" ")
print("siguiente linea")

var = "nombre" 

print(var,type(var))
print(len(var))


"""
while(True):
    var2 = input("ingrese una palabra: ")

    if(var == var2):
        print("Usted descubrio el mensaje oculto")
        break
    else:
        print("palabra equivocada")
    
"""

#Funcion Index
LetrasDelAlfabeto = " abcdefghijklmnñopqrstuvwxyz"
x=input("Ingresa una letra en minuscula del alfabeto para conocer su lugar en el alfabeto: ")
print("")
print(LetrasDelAlfabeto.index(x))
#Funcion Isalnum
y=input("Ingresa una palabra o frase para verificar si solo cuenta con numeros y/o letras: ")
print("")
print(y.isalnum())