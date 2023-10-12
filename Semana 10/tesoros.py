#En una matriz de 3x3 se esconden tesoros y minas.
#Te reto a encontrar los tres tesoros antes de que encuentres
#dos minas.

def buscarTesoros():
    contadorMinas=0
    contadorTesoros=0
    while contadorMinas<2 or contadorTesoros<3:  
       fila=int(input("Digite la fila que desea ver:"))
       col=int(input("Digite la columna que desea ver:"))
       if matrizJuego[fila][col]=="t":
          contadorTesoros=contadorTesoros+1
          print("Felicidades encontraste un tesoro!!!...")
       elif matrizJuego[fila][col]=="m":
          contadorMinas=contadorMinas+1
          print("Cuidado!!!! Caíste en campo minado...")
       if contadorMinas==2:
          print("Lo siento, has perdido...")
       if contadorTesoros==3:
          print("Ganaste!!! Felicidades") 

matrizJuego=[["t","m","t"],["m","m","t"],["m","m","m"]]

fila=0
col=0
buscarTesoros()
