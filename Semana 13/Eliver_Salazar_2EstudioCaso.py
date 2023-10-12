def abrirArchivo():
    return open("registros.txt", "w")

def cerrarArchivo(archivo):
    archivo.close()

def imprimirRegistros():
    archivo = abrirArchivo()
    for profesor in profesores:
        archivo.write(f"numeroEmpleado: {profesor[0]}\n")
        archivo.write(f"nombreCompleto: {profesor[1]}\n")
        archivo.write(f"nacionalidad: {profesor[2]}\n")
        archivo.write(f"departamento: {profesor[3]}\n")
        archivo.write(f"gradoAcademico: {profesor[4]}\n")
        archivo.write(f"aniosLaborados: {profesor[5]}\n")
        archivo.write(f"salario: {profesor[6]}\n")
        archivo.write(f"horariosClases: {profesor[7]}\n")
        archivo.write("\n")
    cerrarArchivo(archivo)
    print("Registros impresos en el archivo 'registros.txt'.")

def registrarProfesor():
    while True:
        try:
            numeroEmpleado = int(input("Ingrese el número de empleado: "))
            nombreCompleto = str(input("Ingrese el nombre completo del profesor: "))
            nacionalidad = str(input("Ingrese la nacionalidad del profesor: "))
            departamento = str(input("Ingrese el departamento del profesor: "))
            
            while True:
                gradoAcademico = str(input("Ingrese el grado académico del profesor (Bachiller o Licenciatura): "))
                if gradoAcademico == 'Bachiller' or gradoAcademico == 'Licenciatura':
                    break
                else:
                    print("Error: Ingrese 'Bachiller' o 'Licenciatura' como opciones válidas.")
            
            aniosLaborados = int(input("Ingrese los años laborados del profesor: "))
            salario = float(input("Ingrese el salario del profesor: $"))
            
            while True:
                horariosClases = str(input("Ingrese los horarios de clases del profesor (Mañana/Tarde/Noche): "))
                if horariosClases == 'Mañana' or horariosClases == 'Tarde' or horariosClases == 'Noche':
                    break
                else:
                    print("Error: Ingrese 'Mañana', 'Tarde' o 'Noche' como opciones válidas.")
            
            profesor = [numeroEmpleado, nombreCompleto, nacionalidad, departamento, gradoAcademico, aniosLaborados, salario, horariosClases]
            profesores.append(profesor)

            print("Registro de profesor exitoso.")
            break
        except ValueError:
            print("Error: Ingrese su información correctamente.")

def consultarProfesor():
    numeroEmpleado = int(input("Ingrese el número de empleado del profesor a consultar: "))
    for profesor in profesores:
        if profesor[0] == numeroEmpleado:
            return profesor
    return None

def menu():
    print("\n*************** REGISTRO PROFESORES UFIDE ***************\n")


    while True:
        print("----- Menú -----")
        print("1. Registro de Profesores")
        print("2. Consulta de Profesores")
        print("3. Impresión de Registros")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrarProfesor()
        elif opcion == "2":
            profesor = consultarProfesor()
            if profesor:
                print("\nInformación del Profesor:")
                print(f"numeroEmpleado: {profesor[0]}")
                print(f"nombreCompleto: {profesor[1]}")
                print(f"nacionalidad: {profesor[2]}")
                print(f"departamento: {profesor[3]}")
                print(f"gradoAcademico: {profesor[4]}")
                print(f"aniosLaborados: {profesor[5]}")
                print(f"salario: {profesor[6]}")
                print(f"horariosClases: {profesor[7]}")
            else:
                print("No se encontró un profesor con ese número de empleado.")
        elif opcion == "3":
            imprimirRegistros()
            print("Registros impresos en el archivo 'registros.txt'.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    profesores = []
    menu()



