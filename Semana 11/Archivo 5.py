
##NombreArchivo = open("NombreArchivo.ext","MododeApertura")


#Todos los import van de primero luego las variables

import os
file = open("miarchivo.txt","r")
mensaje = file.read()
valores = mensaje.split("\n")
for i in valores:
    print (i)
print(valores)
file.close()
