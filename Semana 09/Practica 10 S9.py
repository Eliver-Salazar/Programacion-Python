#Ejercicio 1 semana 9 Arreglos Unidimensionales Ejercicio #1 pag16

DiasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MontoTotal = 0
MenorGanancia = -1
DiaMenorGanancia = ""

for i in range(len(DiasSemana)):
    Dia = DiasSemana [i]
    Monto = float(input(f"Ingrese el monto ganado en {Dia}: $"))
    MontoTotal += Monto
    
    if MenorGanancia == -1 or Monto < MenorGanancia:
        MenorGanancia = Monto
        DiaMenorGanancia = Dia

print("El monto total ganado en la semana es: $",MontoTotal)
print("El día en el que ganó menos dinero fue: ",DiaMenorGanancia, "por: $", MenorGanancia)





