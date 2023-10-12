def mostrar():
   for x in range(0,3):
       for y in range(0,3):
           print(puntosJuego[x][y],end=' ')
       print("\n")    


x=0
y=0
puntosJuego=[[23,54,12],[21,81,14],[16,20,21]]
mostrar()
print("La posición 0,1 contiene:",puntosJuego[0][1])
x=int(input("Digite la posición de la fila que desea ver:"))
y=int(input("Digite la posición de la columna que desea ver:"))
print("La posición ",x,",",y," contiene:",puntosJuego[x][y])
