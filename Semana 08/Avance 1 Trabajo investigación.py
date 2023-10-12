#Ingreso Usuario

Usuario = ""
Contraseña = ""

while Usuario != "admin" or Contraseña != "Adm115":
    Usuario = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    if Usuario == "admin" and Contraseña == "Adm115":
        print("Inicio de sesión exitoso. Bienvenido, administrador.")
    else:
        print("Error, intente nuevamente.")

#Menú

Opcion = ""

while Opcion != "4":
    print("\n----- Menú -----")
    print("1. Registro de dueño")
    print("2. Registro de mascota")
    print("3. Agenda de cita")
    print("4. Salir")

    Opcion = input("Seleccione una opción: ")

# Registro dueño

    if Opcion == "1":
        Nombre_dueño = input("\nIngrese el nombre completo del dueño: ")
        Cedula_dueño = input("Ingrese la cédula del dueño: ")
        Telefono_dueño = input("Ingrese el número de teléfono del dueño: ")
        Correo_dueño = input("Ingrese el correo del dueño: ")
        Direccion_dueño = input("Ingrese la dirección del dueño: ")

# Registro mascota

    elif Opcion == "2":
        Nombre_mascota = input("\nIngrese el nombre de la mascota: ")
        Raza_mascota = input("Ingrese la raza de la mascota: ")
        Fecha_nacimiento = input("Ingrese la fecha de nacimiento de la mascota: ")
        Sexo_mascota = input("Ingrese el sexo de la mascota: ")
        Peso_mascota = (input("Ingrese el peso de la mascota: "))
        Caracteristicas_mascota = input("Ingrese las características de la mascota: ")
        Alimento_mascota = input("Ingrese el alimento que consume la mascota: ")
        Observaciones_mascota = input("Ingrese las observaciones generales de la mascota: ")

# Registro Cita

    elif Opcion == "3":
        Turno_cita = input("\nIngrese el turno de la cita: ")
        Horario_cita = input("Ingrese el horario de la cita: ")
        Fecha_cita = input("Ingrese la fecha de la cita: ")
        Especialidad_cita = input("Ingrese la especialidad o tratamiento requerido: ")
        Medico_asignado = input("Ingrese el nombre del médico asignado: ")

# Salida

    elif Opcion == "4":
        print("\nGracias por utilizar el sistema. Hasta luego.")

    else:
        print("\nOpción inválida. Por favor, seleccione una opción válida.")


