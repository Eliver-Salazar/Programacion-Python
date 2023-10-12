
#Definicion de variables

a=0
b=0

#Entrada de datos

print("Estos es una caculadora que hara las 4 operaciones basicas con los/nnumeros que usted ingrese")
a=(int)(input("Ingrese el primer numero: "))
b=(int)(input("Ingrese el segundo numero: "))
      
#Proceso de datos

if a == 0 or b == 0:
    print("Ingrese un numero valido, no 0")
    a=(int)(input("Ingrese el primer numero: "))
    b=(int)(input("Ingrese el segundo numero: "))
    suma = a+b
    resta = a-b
    division = a/b
    multiplicacion = a*b
else:
    suma = a+b
    resta = a-b
    division = a/b
    multiplicacion = a*b

#Salida de datos

print("El resultado de las operaciones es: "
      ,"\n Suma:",suma
      ,"\n","Resta:",resta
      ,"\n","Division:",division
      ,"\n","Multiplicacion:",multiplicacion)

