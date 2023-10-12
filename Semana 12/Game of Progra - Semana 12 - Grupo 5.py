#Menu estudiantes y calificaciones

def agregar_informacion():
    nombre = input("Ingrese el nombre del estudiante: ")
    grupo = input("Ingrese el número de grupo: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    file = open("miarchivo.txt", "a")
    file.write(f"{nombre},{grupo},{calificacion}\n")
    file.close()
    print("Información agregada correctamente.")

def mostrar_informacion():
    print("\n--- Información de estudiantes ---")
    file = open("miarchivo.txt", "r")
    for line in file:
        nombre, grupo, calificacion = line.split(',')
        print(f"Nombre: {nombre}, Grupo: {grupo}, Calificación: {calificacion}")
    file.close()

def menu():
    while True:
        print("\n----- Menú -----")
        print("1. Agregar información de estudiante")
        print("2. Mostrar información de estudiantes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for _ in range(10):
                agregar_informacion()
        elif opcion == "2":
            mostrar_informacion()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()

