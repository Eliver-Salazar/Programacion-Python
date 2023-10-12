#Ejercicio 1 semana 9 Arreglos Unidimensionales Ejercicio #1 pag16


DiaSem = ["Lunes","Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
CantKm = {}
Suma = 0
for i in range(0,7):
    Valor = int(input(f"Ingrese la cantidad de km recorridos día {DiaSem [i]}: "))
    CantKm [i] = Valor
    Suma += Valor
for i in range(0,len(CantKm)):
    print (CantKm [i],DiaSem [i] , end = " ")
print("La cantidad", Suma)






