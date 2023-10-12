def llenarMatriz():
    for x in range(5):
        notas.append([0]*4)

def agregarValores():
    for x in range(0,5):
        for y in range(0,4):
            notas[x][y]=int(input("Ingrese la nota obtenida:"))

def mostrarMatriz():
    for x in range(0,5):
        for y in range(0,4):
            print(notas[x][y],end=" ")
        print("\n")

def calcularPromedio():
    sumaNotas=0
    cantNotas=0
    promedioNotas=0
    for x in range(0,5):
        for y in range(0,4):
            sumaNotas=sumaNotas+notas[x][y]
            cantNotas=cantNotas+1
    promedioNotas=sumaNotas/cantNotas
    print("La calificación promedio del grupo es de:",promedioNotas)    
            
def modificarNota():
    x=int(input("Digite el valor de la fila que desea modificar:"))
    y=int(input("Digite el valor de la columna que desea modificar:"))
    nuevaCalificacion=int(input("Digite la nueva calificación:"))    
    notas[x][y]=nuevaCalificacion

x=0
y=0
notas=[]
llenarMatriz()
agregarValores()
mostrarMatriz()
calcularPromedio()
modificarNota()
mostrarMatriz()
