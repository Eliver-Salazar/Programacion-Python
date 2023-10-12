#INSTRUCCION SIMPLE SEMANA 4 PAG 29

#Asignacion de la variable
Num1 = 0
Num2 = 0
Num3 = 0

# Solicitar los tres números al usuario
Num1 = int(input("Ingrese el primer número: "))
Num2 = int(input("Ingrese el segundo número: "))
Num3 = int(input("Ingrese el tercer número: "))

#Proceso de datos
if Num1 >= Num2 and Num1 >= Num3:
    if Num2 >= Num3:
        print("El orden de los números de forma descendente son:", Num1, Num2, Num3)
    else:
        print("El orden de los números de forma descendente son:", Num1, Num3, Num2)
elif Num2 >= Num1 and Num2 >= Num3:
    if Num1 >= Num3:
        print("El orden de los números de forma descendente son:", Num2, Num1, Num3)
    else:
        print("El orden de los números de forma descendente son:", Num2, Num3, Num1)
else:
    if Num2 >= Num1:
        print("El orden de los números de forma descendente son:", Num3, Num2, Num1)
    else:
        print("El orden de los números de forma descendente son:", Num3, Num1, Num2)

#Salida de datos


