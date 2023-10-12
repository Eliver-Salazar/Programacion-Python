#INSTRUCCION SIMPLE SEMANA 4 PAG 17


#Asignacion de la variable 
Salario = 0
Incremento = 0

#Entrada de datos
Salario = int(input("Ingrese el monto de su salario: "))


#Proceso de datos
if Salario < 1000:
    Incremento = Salario * 0.15
Total = Salario + Incremento

#Salida de datos    
print ("El total de su salario corresponde a:", Total, "dólares")
