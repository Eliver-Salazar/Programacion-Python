#Ejercicio 1 semana 9 Arreglos Unidimensionales Ejercicio #1 pag16

PalabraReves = ""

Palabra = input("Ingrese una palabra: ")

for i in range(len(Palabra)-1,-1,-1):
    PalabraReves += Palabra[i]

print("La palabra al revés es:", PalabraReves)

