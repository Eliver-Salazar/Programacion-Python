#ESTRUCTURA SEMANA 6 EJERCICIO #2

#Variables
EstaturaMenor_100 = 0
Estatura_100_120 = 0
Estatura_121_130 = 0
Estatura_131_140 = 0
EstaturaMayor_140 = 0
SumaEstaturas = 0

#Entrada de datos

CantNiños = int(input("Ingrese la cantidad de niños a los cuales desea evaluar su estatura: "))

#Proceso de datos

for i in range(CantNiños):
    Estatura = float(input(f"Ingrese la estatura del niño {i+1}: "))
    if Estatura < 100:
        EstaturaMenor_100 += 1
    elif Estatura >= 100 and Estatura <= 120:
        Estatura_100_120 += 1
    elif Estatura >= 121 and Estatura <= 130:
        Estatura_121_130 += 1
    elif Estatura >= 131 and Estatura <= 140:
        Estatura_131_140 += 1
    else:
        EstaturaMayor_140 += 1
    SumaEstaturas += Estatura

PromedioEstaturas = SumaEstaturas / CantNiños

#Salida de datos

print("Cantidad de niños que miden menos de 100 cm:", EstaturaMenor_100)
print("Cantidad de niños que miden entre 100 y 120 cm:", Estatura_100_120)
print("Cantidad de niños que miden entre 121 y 130 cm:", Estatura_121_130)
print("Cantidad de niños que miden entre 131 y 140 cm:", Estatura_131_140)
print("Cantidad de niños que miden más de 140 cm:", EstaturaMayor_140)
print("Promedio de estaturas:", PromedioEstaturas)









