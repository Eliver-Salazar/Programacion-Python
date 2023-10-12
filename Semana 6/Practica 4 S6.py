#ESTRUCTURA SEMANA 6 EJERCICIO #4


#Variables

Salario = 0
Diferencia = 0
DineroNecesario = 0

#Entrada y proceso de datos

for i in range (15):
    Salario = int(input(f"Ingrese un monto {i+1}: "))
    if Salario < 500:
        Diferencia = 500 - Salario
        DineroNecesario = DineroNecesario + Diferencia
        print("Para que su salario llegue a $500 le faltan: ", Diferencia)
        
    else:
        print("Su salario se encuentra correctamente")

#Salida de datos

print("La diferencia para que a menos todos ganen 500 es de: ",DineroNecesario)


        















