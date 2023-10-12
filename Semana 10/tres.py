def llenarMatriz():
    for x in range(0,3):
        numeros.append([0]*3)

def mostrarMatriz():
    print("La matriz contiene:\n")
    for x in range(0,3):
        for y in range(0,3):
            print(numeros[x][y],end=" ")
        print("\n")

def agregarValores():
    for x in range(0,3):
        for y in range(0,3):
            numeros[x][y]=int(input("Digite un número entero:"))

def sumarDatos():
    sumaFila0=0
    sumaFila1=0
    sumaFila2=0
    sumaCol0=0
    sumaCol1=0
    sumaCol2=0
    sumaDiagP=0
    sumaDiagS=0
    for y in range(0,3):
        sumaFila0=sumaFila0+numeros[0][y]
        sumaFila1=sumaFila1+numeros[1][y]
        sumaFila2=sumaFila2+numeros[2][y]
    for x in range(0,3):
        sumaCol0=sumaCol0+numeros[x][0]
        sumaCol1=sumaCol1+numeros[x][1]
        sumaCol2=sumaCol2+numeros[x][2]
    for x in range(0,3):
        for y in range(0,3):
            if x==y: 
               sumaDiagP=sumaDiagP+numeros[x][y]
    for x in range(0,3):
        for y in range(0,3):
            if (x+y)==3-1: 
               sumaDiagS=sumaDiagS+numeros[x][y]   
    print("*****Resultados*****\n")
    print("La suma de la fila 0 es:",sumaFila0)
    print("La suma de la fila 1 es:",sumaFila1)
    print("La suma de la fila 2 es:",sumaFila2)
    print("La suma de la columna 0 es:",sumaCol0)
    print("La suma de la columna 1 es:",sumaCol1)
    print("La suma de la columna 2 es:",sumaCol2)
    print("La suma de la diagonal principal es:",sumaDiagP)
    print("La suma de la diagonal secundaria es:",sumaDiagS)

x=0
y=0
numeros=[]
llenarMatriz()
mostrarMatriz()
agregarValores()
mostrarMatriz()
sumarDatos()
