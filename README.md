#Autor: Juan Eduardo Franco A.
#1 Funciones con  rindex

texto = "Hola Mundo, Hola Python"

# Encontrar la última ocurrencia de "Hola"
try:
    indice = texto.rindex("Hola")  
# Busca la última ocurrencia de "Hola"

    print("Última ocurrencia de 'Hola' comienza en el índice:", indice)
except ValueError:
    print("La subcadena 'Hola' no se encuentra en el texto.")


#2 Funcion con rindex 

Url = "https:/www.ejemplo.com/imagen/imagen.jpg"
Ultimo_slash = Url.rindex("/")
Archivo = Url[Ultimo_slash + 1:]
#Extrae todo despues del ultimo "/"
print(Archivo)





#3 Funcion con rindex 

texto = "Python es un lenguaje poderoso"
ultimo_espacio = texto.rindex(" ")  
# Encuentra el último espacio
ultima_palabra = texto[ultimo_espacio + 1:]
print(ultima_palabra)  




#4 Funcion con rindex 

Registro = "Nombre, apellido, edad, profesion"
Ultima_coma = Registro.rindex(",")
#Encuentra la ultima coma
Ultimo_campo =  Registro[Ultima_coma + 1:]
print(Ultimo_campo)


#1 Funcion con rfind

Numero_producto = "producto-12345-67890"
ultimo_guion = Numero_producto.rfind("-") 
#Encuentra el último guion

base_id = Numero_producto[:ultimo_guion]  
#Extrae todo antes del último guion

print(base_id) 



#2 funcion con rfind 

fecha = "2025-09-14"
pos = fecha.rfind("-")
dia = fecha[pos + 1:]
print("Día:", dia)  



#3 funcion con rfind 


frase = "Programar es divertido"
for vocal in "aeiou":
    pos = frase.rfind(vocal)
    if pos != -1:
        print(f"Última '{vocal}' en posición {pos}")




#4 funcion con rfind 

email = "Eduardo_unal@python.com"
pos = email.rfind("@")
usuario = email[:pos]
print("Usuario:", usuario)
