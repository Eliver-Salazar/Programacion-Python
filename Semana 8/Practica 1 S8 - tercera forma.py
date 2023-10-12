#Ejercicio 1 semana 8

#Asignación de variables

a = 0
b = 0

#Definición de funciones (Subprocesos)

def Suma(a,b):
    Resultado = a + b
    return Resultado

def Resta(a,b):
    Resultado1 = a - b
    return Resultado1

def Multiplicacion(a,b):
    Resultado2 = a * b
    return Resultado2

def Division(a,b):
    Resultado3 = a / b
    return Resultado3

#Entrada de datos

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

#Salida de datos

Resultado = Suma(a,b)
Resultado1 = Resta(a,b)
Resultado2 = Multiplicacion(a,b)
Resultado3 = Division(a,b)

print("La suma es:",Resultado)
print("La resta es:",Resultado1)
print("La multiplicación es:",Resultado2)
print("La división es:",Resultado3)
