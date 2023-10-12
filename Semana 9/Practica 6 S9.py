#Ejercicio 1 semana 9 Arreglos Unidimensionales

PuntosJuegos ={}
for i in range (0,10):
    Valor = int (input("Ingrese la puntuación obtenida: "))
    PuntosJuegos [i] = Valor

for i in range (0, len(PuntosJuegos)):
    print (PuntosJuegos [i], end = " ")

print(PuntosJuegos)
