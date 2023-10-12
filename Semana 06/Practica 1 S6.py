#ESTRUCTURA SEMANA 6 EJERCICIO #1

#Variables

TiempoVuelta = 0
TiempoPits = 0
SumatoriaVuelta = 0
SumatoriaPits = 0

#Proceso de datos

for i in range (10):
    TiempoVuelta = float(input(f"Ingrese el tiempo realizado por vuelta {i+1}: "))
    SumatoriaVuelta = SumatoriaVuelta + TiempoVuelta

for i in range (10):
    TiempoPits = float(input(f"Ingrese el tiempo utilizado en Pits {i+1}: "))
    SumatoriaPits = SumatoriaPits + TiempoPits

#Promedios

PromedioVuelta = SumatoriaVuelta / 10
PromedioPits = SumatoriaPits / 10
Porcentaje = (PromedioPits / PromedioVuelta) * 100

#Salida de datos

print("El tiempo promedio por vuelta es de:",PromedioVuelta)
print("El tiempo promedio por pits es de:",PromedioPits)
print("El porcentaje de tiempo PITS respecto al tiempo de vuelta:",Porcentaje)





