#Ejercicio 1 semana 8

#Asignación de variables

a = 0
b = 0

#Definición de funciones (Subprocesos)

def Suma(a,b):
    Resultado = a + b
    return Resultado

def Resta(a,b):
    Resultado = a - b
    return Resultado

def Multiplicacion(a,b):
    Resultado = a * b
    return Resultado

def Division(a,b):
    Resultado = a / b
    return Resultado

#Entrada de datos

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

#Salida de datos

Resultado = Suma(a,b)
print("La suma es:",Resultado)
print("La resta es:",Resta(a,b))
print("La multiplicación es:",Multiplicacion(a,b))
print("La división es:",Division(a,b))
