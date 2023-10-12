#Ejercicio 1 semana 9 Arreglos Unidimensionales Ejercicio #1 pag16

Kilometros = {}
Suma = 0

for i in range (0,7):
    Recorrido = float(input("Ingrese los kilómetros recorridos por día: "))
    Kilometros [i] = Recorrido
    #Suma = Suma + Recorrido
    Suma += Recorrido

for i in range (0,len(Kilometros)):
    print(Kilometros [i], end = " ,")

print("\nLa sumatoria de todos los kilómetros es: ", Suma)
