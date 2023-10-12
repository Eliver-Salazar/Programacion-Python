#ESTRUCTURAS DE REPETICION WHILE SEMANA 5 PAG 14

NotaMayor = 0
NotaMenor = 100
CantAprobados = 0
CantReprobados = 0
Contador = 0


CantAlumnos = int(input("Ingrese la cantidad de alumnos: "))


while Contador < CantAlumnos:
    Nota = int(input("Ingrese la nota del alumno: "))
    
    if Nota > NotaMayor:
        NotaMayor = Nota
    
    if Nota < NotaMenor:
        NotaMenor = Nota
    
    if Nota >= 70:
        CantAprobados += 1
    else:
        CantReprobados += 1
    
    Contador += 1

print("La nota mayor es:", NotaMayor)
print("La nota menor es:", NotaMenor)
print("La cantidad de aprobados es:", CantAprobados)
print("La cantidad de reprobados es:", CantReprobados)







