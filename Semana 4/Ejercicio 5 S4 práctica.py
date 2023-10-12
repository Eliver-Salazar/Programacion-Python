#INSTRUCCION SIMPLE SEMANA 4 PAG 21


#Asignacion de la variable 
Salario = 0
Incremento = 0
Total = 0

#Entrada de datos
Salario = int(input("Ingrese el monto de su salario: "))

#Proceso de datos
if Salario > 1000:
    Incremento = Salario * 0.15
    print ("Su incremento del 15% ha sido por:", Incremento, "dólares")
    
else:
    Incremento = Salario * 0.20
    print ("Su incremento del 20% ha sido por:", Incremento, "dólares")

    
Total = Salario + Incremento


#Salida de datos    
print ("Para un total correspondiente a su nuevo salario por:", Total, "dólares")
