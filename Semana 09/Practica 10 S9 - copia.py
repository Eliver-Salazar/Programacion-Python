#Ejercicio 1 semana 9 Arreglos Unidimensionales Ejercicio #1 pag16

MontoTotal = -1
MenorGanancia = -1


Monto = float(input(f"Ingrese el monto ganado:"))
MontoTotal += Monto
    
if MontoTotal == -1 or Monto < MenorGanancia:
    MontoTotal = Monto
    
print("El monto total ganado en la semana es: $",MontoTotal)
