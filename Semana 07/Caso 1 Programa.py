#Solicitar cantidad de empleados

n = int(input("Ingrese la cantidad de empleados: "))

#Variables
CantHombres = 0
CantMujeres = 0
MujeresMas_20k = 0
HombresMenores_40k = 0
EmpleadosMayores_50 = 0


#Proceso de Datos
i = 0
while i < n:
    print(f"\nEmpleado {i+1}:")
    
    Identificacion = int(input("Ingrese la identificación: "))
    Edad = int(input("Ingrese la edad: "))
    Genero = (input("Ingrese el género (M/F): "))
    Sueldo = float(input("Ingrese el sueldo: "))
    if Genero == "M":
        CantHombres += 1
    elif Genero == "F":
        CantMujeres += 1

    if Genero == "F" and Sueldo > 20000:
        MujeresMas_20k += 1

    if Genero == "M" and Edad < 40 and Sueldo < 40000:
        HombresMenores_40k += 1

    if Edad > 50:
        EmpleadosMayores_50 += 1

    i += 1

# Salida da Datos
print("\nResultados:")
print("Cantidad de hombres:", CantHombres)
print("Cantidad de mujeres:", CantMujeres)
print("Cantidad de mujeres que ganan más de $20.000:", MujeresMas_20k)
print("Cantidad de hombres menores de 40 años que ganan menos de $40.000:", HombresMenores_40k)
print("Cantidad de empleados mayores a 50 años:", EmpleadosMayores_50)
