#Ejercicio 1 semana 9 Arreglos Unidimensionales Ejercicio #1 pag16


Nombre = {}

for i in range (0,10):
    print("Número de butaca: ", (i+1))
    Valor = input("Ingrese el nombre: ")
    Nombre [i] = Valor
    
for i in range(0,len(Nombre)):
    print()
    print ("Butaca",(i+1),":",Nombre [i])
