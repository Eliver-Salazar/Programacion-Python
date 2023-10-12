#NOVENO EJERCICIO PRACTICA SEMANA 2 -- GASTOS ALIMENTACION


#DEFINICION DE VARIABLES

IngresosMensuales = 0
GastosAlimentacion = 0
Total = 100


#ENTRADA DE DATOS

IngresosMensuales = float(input("Ingrese la cantidad de sus ingresos mensuales:"))
GastosAlimentacion = float(input("Ingrese la cantidad de sus gastos mensuales por alimentacion:"))



#PROCESO DE DATOS

PorcentajeAlimentacion = (GastosAlimentacion / IngresosMensuales) * Total
PorcentajeOtrosRubros = Total - PorcentajeAlimentacion



#SALIDA DE DATOS

print("El porcentaje gastado para la alimentacion es de:",PorcentajeAlimentacion)
print("El porcentaje disponible para otros rubos es de:",PorcentajeOtrosRubros)
