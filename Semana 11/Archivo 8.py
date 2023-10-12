import os
nombres = []

#Se leen los nombre de los alumnos

for i in range(10):
    nombres.append(input("Ingrese su nombre:"))

#Se guardan los datos en un archivo de texto

file = open("nombres.txt","w")
for  nombre in nombres:
    file.write(nombre + "\n" + "\n")
file.close()

#Se leen los datos del archivo y se guardan en un nuevo arreglo

file = open("nombres.txt","r")
datos = file.read()
otros = datos.split("\n")
for i in otros:
    print(i)
print(otros)
file.close()
