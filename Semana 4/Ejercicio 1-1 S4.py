#INSTRUCCION SIMPLE SEMANA 4 PAG 15


#Asignacion de la variable 
Precio = 0
Cantidad = 0

#Entrada de datos
Precio = int(input("Ingrese el precio del producto: "))
Cantidad = int(input("ingrese la cantidad del producto: "))

#Proceso de datos
if Cantidad >= 12:
    Descuento = Precio * 0.8

Total = Descuento * Cantidad

    
#Salida de datos    
print ("El total a pagar es de:", Total)
