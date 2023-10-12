#OCTAVO EJERCICIO PRACTICA SEMANA 2 -- SALARIO MENSUAL


#DEFINICION DE VARIABLES

CantHrsSem = 0
PrecioxHr = 0
SemanasxMes = 4.2
CargasSociales = 0.105
Asociacion = 0.05


#ENTRADA DE DATOS

CantHrsSem = float (input("Ingrese la cantidad de horas semanales trabajadas:"))
PrecioxHr= float(input("Ingrese el precio que se le paga por hora trabajada:"))



#PROCESO DE DATOS

SalarioSem = CantHrsSem * PrecioxHr
SalarioBruto = SalarioSem * SemanasxMes
Deducciones = (SalarioBruto * CargasSociales) + (SalarioBruto * Asociacion)
SalarioNeto = SalarioBruto - Deducciones


#SALIDA DE DATOS

print("El salario neto mensual de la persona trabajadora es de:", SalarioNeto)
