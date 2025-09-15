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

#Isupper

#La funcion de este metodo es verificar si todo el texto esta en mayusculas 
#Si todo el texto esta en mayuscula dara true
'''
text= "CALI"
print(text.isupper())
text2="HOLA MUNDO, ESTOY PROGRAMANDO PYTHON"
print(text2.isupper())
#Si solo esta la primera letra en mayuscula y el resto en minuscula dara False
text3="Cali"
print(text3.isupper())
text4="Hola mundo, estoy programando python"
print(text4.isupper())
#No afecta si hay numeros o simbolos
text5="CALLE 3 N°4"
print(text5.isupper())
text6="¡CARRERA 23 #10¡"
print(text6.isupper())
text7="Calle 3 N°4"
print(text7.isupper())
'''
#Join
#Sirve para contatenar elementos string, no funciona si hay int o float
texto="Hola", "mundo", "Python"
A="".join(texto)
print(A)
Texto2= "Hola", "mundo", "Python"
B=" ".join(Texto2)
print(B)
#En "" puedes agregar los separadores 
Texto3= "Hola", "mundo", "Python"
C="-".join(Texto2)
print(C)
Texto4= "Hola", "mundo", "Python"
D="_".join(Texto4)
print(D)
Texto5= "1" "2" "3"
E=",".join(Texto5)
print(E)
