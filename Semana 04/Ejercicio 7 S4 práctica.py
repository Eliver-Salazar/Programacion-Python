#INSTRUCCION SIMPLE SEMANA 4 PAG 28


#Asignacion de la variable 
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0

#Entrada de datos

Num1 = int(input("Ingrese su primer número: "))
Num2 = int(input("Ingrese su segundo número: "))
Num3 = int(input("Ingrese su tercer número: "))
Num4 = int(input("Ingrese su cuarto número: "))


#Proceso de datos
if Num1 > Num2:
    Mayor1 = Num1
else:
    Mayor1 = Num2
if Num3 > Num4:
    Mayor2 = Num3
else:
    Mayor2 = Num4

#Salida de datos    
print ("El número mayor del primer y segundo número es:",Mayor1,"y el mayor del tercer y cuarto número es",Mayor2,)
