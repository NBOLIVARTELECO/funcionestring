#autor: Andrés F. Núñez
#fecha: 14/09/2025


#Ejercicios de variables y metodos

print("Bienvenido, en el siguiente programa se mostraran ejemplos de como usar los metodos replace, removeprefix, upper y rfind \n")

var=input("primero definimos una variable, puedes escribir una frase o plabra: ")

print("ahora reemplazaremos las a y o por numeros")

if var==(var.replace("a","4").replace("o","0")):
    print("tu frase no tiene las letras a ni o")
    ejem="platano"
    print(f"\nTe dejo un ejemplo: {ejem} -> {ejem.replace('a','4').replace('o','0')}")
else:
    print(var.replace("a","4").replace("o","0"))

print("\nAhora quitaremos el prefijo a tu frase, si lo tiene.")

if var==var.removeprefix("El ").removeprefix("el ").removeprefix("La ").removeprefix("la ").removeprefix("EL ").removeprefix("LA "):
    print("tu frase no tiene un prefijo valido")

    ejem="el tiene frio"
    print(f"\nTe dejo un ejemplo: {ejem} -> {ejem.removeprefix('el ')}")

else:
    print(var.removeprefix("El ").removeprefix("el ").removeprefix("La ").removeprefix("la ").removeprefix("EL ").removeprefix("LA "))


print("\nSeguimos con ejemplos extra")

print("\nCon este se pone en mayusculas", var.upper())
if var==var.upper():
    print("a que está igual.")

print("\nY con este podemos saber donde está la ultima letra a en tu frase")

print(var.rfind("a"))
if var.rfind("a")==-1:
    print("tu frase no tiene la letra a")