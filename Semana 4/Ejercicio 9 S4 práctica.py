#INSTRUCCION SIMPLE SEMANA 4 PAG 30


#Asignacion de la variable 

AñoNac = 0

#Entrada de datos

AñoNac = int(input("Ingrese su año de nacimiento: "))


#Proceso de datos

if (AñoNac % 4 == 0 and AñoNac % 100 != 0) or AñoNac % 400 == 0:
    print("El año",AñoNac,"es un año bisiesto:")
else:
    print("El año",AñoNac,"no es un año bisiesto")


#Salida de datos    

