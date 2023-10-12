#Ejercicio 1 semana 9 Arreglos Unidimensionales

def mostrar ():
    for x in range (0,3):
        for y in range (0,3):
            print (PuntosJuego[x][y], end = ' ' )
        print ("\n")

x = 0
y = 0

PuntosJuego = [[23, 54, 12] , [21, 81, 14] , [16, 20, 21]]
mostrar ()
print ("Esta posición 0, 1 contiene: ", PuntosJuego[0][1])
