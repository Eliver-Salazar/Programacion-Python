#ESTRUCTURA ANIDADO SEMANA 4 PAG 23


#Asignacion de la variable 
Nota = 0

#Entrada de datos

Nota = int(input("Ingrese su nota: "))

#Proceso de datos

if Nota >= 70:
    print ("Ha aprobado")
    
else:
    if Nota >= 60:
        print ("Ha aplazado")
    else:
        print ("Ha reprobado")       
    
#Salida de datos
print ("Nos vemos....")
