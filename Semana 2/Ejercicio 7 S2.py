#QUINTO EJERCICIO PRACTICA SEMANA 2 -- AREA Y PERIMETRO RECTANGULO


#DEFINICION DE VARIABLES

EdadPersona1 = 0
EdadPersona2 = 0
EdadPersona3 = 0
EdadPersona4 = 0
EdadPersona5 = 0
Promedio = 5

#ENTRADA DE DATOS

EdadPersona1 = int (input("Ingrese la edad de la primera persona:"))
EdadPersona2 = int (input("Ingrese la edad de la segunda persona:"))
EdadPersona3 = int (input("Ingrese la edad de la tercer persona:"))
EdadPersona4 = int (input("Ingrese la edad de la cuarta persona:"))
EdadPersona5 = int (input("Ingrese la edad de la quinta persona:"))


#PROCESO DE DATOS

SumasEdad = (EdadPersona1 + EdadPersona2 + EdadPersona3 + EdadPersona4 + EdadPersona5)
EdadPromedio = SumasEdad / Promedio

#SALIDA DE DATOS

print("La edad promedio de las 5 personas es de:", EdadPromedio)
