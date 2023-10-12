#ESTRUCTURA ANIDADO SEMANA 4 PAG 24


#Asignacion de la variable 

Salario = 0
Categoria = 0
Incremento = 0

#Entrada de datos

Salario = int(input("Ingrese el monto de su salario: "))
Categoria = int(input("Ingrese el valor de su categoría,(Valores del 1 al 4): "))

#Proceso de datos

if Categoria == 1:
    Incremento = Salario * 0.10
    print ("Su incremento del 10% ha sido por:", Incremento, "dólares")
    
elif Categoria == 2:
    Incremento = Salario * 0.12
    print ("Su incremento del 12% ha sido por:", Incremento, "dólares")

elif Categoria == 3:
    Incremento = Salario * 0.15
    print ("Su incremento del 15% ha sido por:", Incremento, "dólares")

else:
    Incremento = Salario * 0.20
    print ("Su incremento del 20% ha sido por:", Incremento, "dólares")


Total = Salario + Incremento
    
#Salida de datos
print ("Para un total correspondiente a su nuevo salario por:", Total, "dólares")
