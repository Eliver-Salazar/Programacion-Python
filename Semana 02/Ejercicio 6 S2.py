#SEXTO EJERCICIO PRACTICA SEMANA 2 -- COSTO TOTAL


#DEFINICION DE VARIABLES

DistanciaEnKm = 0
CostoxKm = 0
CantDiasxSem = 0
SemxCuatrimestre = 15

#ENTRADA DE DATOS

DistanciaEnKm = int (input("Ingrese la distancia recorrida de su casa a la universidad en kilómetros:"))
CostoxKm = int (input("Ingrese el costo por kilómetro recorrido de su medio de transporte:"))
CantDiasxSem = int (input("Ingrese la cantidad de días a la semana que viaja a la universidad:"))

#PROCESO DE DATOS

IdayVueltaxSem = CantDiasxSem * 2
IdayVueltaxCuatri = IdayVueltaxSem * SemxCuatrimestre
CostoTotal= IdayVueltaxCuatri * DistanciaEnKm * CostoxKm

#SALIDA DE DATOS

print("El costo total por trasladarse por cuatrimestre es de", CostoTotal)
