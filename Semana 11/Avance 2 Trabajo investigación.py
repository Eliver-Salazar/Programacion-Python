# Ingreso Usuario

Usuario = ""
Contraseña = ""

while Usuario != "admin" or Contraseña != "Adm115":
    Usuario = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    if Usuario == "admin" and Contraseña == "Adm115":
        print("Inicio de sesión exitoso. Bienvenido, administrador.")
    else:
        print("Error, intente nuevamente.")

# Menú

Opcion = ""
Dueños = []
Mascotas = []
Citas = []

while Opcion != "7":
    print("\n----- Menú -----")
    print("1. Registro de dueño")
    print("2. Registro de mascota")
    print("3. Agenda de cita")
    print("4. Módulo de Vacunación")
    print("5. Módulo de Facturación")
    print("6. Módulo de Reportes")
    print("7. Salir")

    Opcion = input("Seleccione una opción: ")

    # Registro dueño
    if Opcion == "1":
        Nombre_dueño = input("\nIngrese el nombre completo del dueño: ")
        Cedula_dueño = input("Ingrese la cédula del dueño: ")
        Telefono_dueño = input("Ingrese el número de teléfono del dueño: ")
        Correo_dueño = input("Ingrese el correo del dueño: ")
        Direccion_dueño = input("Ingrese la dirección del dueño: ")
        Dueño = {
            "Nombre": Nombre_dueño,
            "Cédula": Cedula_dueño,
            "Teléfono": Telefono_dueño,
            "Correo": Correo_dueño,
            "Dirección": Direccion_dueño
        }
        Dueños.append(Dueño)
        print("Registro de dueño exitoso.")

    # Registro mascota
    elif Opcion == "2":
        Nombre_mascota = input("\nIngrese el nombre de la mascota: ")
        Raza_mascota = input("Ingrese la raza de la mascota: ")
        Fecha_nacimiento = input("Ingrese la fecha de nacimiento de la mascota: ")
        Sexo_mascota = input("Ingrese el sexo de la mascota: ")
        Peso_mascota = input("Ingrese el peso de la mascota: ")
        Caracteristicas_mascota = input("Ingrese las características de la mascota: ")
        Alimento_mascota = input("Ingrese el alimento que consume la mascota: ")
        Observaciones_mascota = input("Ingrese las observaciones generales de la mascota: ")
        Mascota = {
            "Nombre": Nombre_mascota,
            "Raza": Raza_mascota,
            "Fecha de nacimiento": Fecha_nacimiento,
            "Sexo": Sexo_mascota,
            "Peso": Peso_mascota,
            "Características": Caracteristicas_mascota,
            "Alimento": Alimento_mascota,
            "Observaciones": Observaciones_mascota
        }
        Mascotas.append(Mascota)
        print("Registro de mascota exitoso.")

    # Registro Cita
    elif Opcion == "3":
        Turno_cita = input("\nIngrese el turno de la cita: ")
        Horario_cita = input("Ingrese el horario de la cita: ")
        Fecha_cita = input("Ingrese la fecha de la cita: ")
        Especialidad_cita = input("Ingrese la especialidad o tratamiento requerido: ")
        Medico_asignado = input("Ingrese el nombre del médico asignado: ")
        Cita = {
            "Turno": Turno_cita,
            "Horario": Horario_cita,
            "Fecha": Fecha_cita,
            "Especialidad": Especialidad_cita,
            "Médico asignado": Medico_asignado
        }
        Citas.append(Cita)
        print("Agenda de cita exitosa.")

    # Módulo de Vacunación
    elif Opcion == "4":
        Medicamento_vacuna = input("Ingrese el medicamento a aplicar: ")
        Fecha_colocacion = input("Ingrese la fecha de colocación de la vacuna: ")
        Dosis_vacuna = input("Ingrese la dosis de la vacuna: ")
        Proxima_cita = input("Ingrese la fecha de la próxima cita de vacunación: ")

        

    # Módulo de Facturación
    elif Opcion == "5":
        Mombre_cliente = input("Ingrese el nombre del cliente: ")

        # Inicializar listas para almacenar los detalles de la factura
        Descripcion = []
        Cantidad = []
        Precio = []
        Subtotal = []

        # Ciclo para agregar productos a la factura
        while True:
            Descripcion_producto = input("Ingrese la descripción del producto o 'fin' para terminar: ")
            if Descripcion_producto.lower() == "fin":
                break

            Cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            Precio_producto = float(input("Ingrese el precio del producto: "))
            Subtotal_producto = Cantidad_producto * Precio_producto

            Descripcion.append(Descripcion_producto)
            Cantidad.append(Cantidad_producto)
            Precio.append(Precio_producto)
            Subtotal.append(Subtotal_producto)

        Total_general = sum(Subtotal)
        Fescuento = total_general * 0.10  # Suponiendo un descuento del 10% para fines ilustrativos
        Iva = Total_general * 0.12  # Suponiendo un IVA del 12% para fines ilustrativos
        # Imprimir la factura
        print("------ Factura ------")
        print(f"Nombre del Cliente: {Nombre_cliente}")
        print("Descripción | Cantidad | Precio | Subtotal")
        for i in range(len(descripcion)):
            print(f"{Fescripcion[i]} | {Cantidad[i]} | ${Precio[i]:.2f} | ${Subtotal[i]:.2f}")
        print(f"Descuento: ${Descuento:.2f}")
        print(f"IVA: ${Iva:.2f}")
        print(f"Total General: ${Total_general + Iva - Descuento:.2f}")

    # Módulo de Reportes
    elif Opcion == "6":
        print("----- Módulo de Reportes -----")
        print("1. Listado de las citas programadas para servicios y vacunación")
        print("2. Listado de las citas programadas")
        print("3. Listado de los productos y/o servicios ofrecidos por semana o mes")
        Reporte_opcion = input("Seleccione una opción de reporte: ")

        if Reporte_opcion == "1":
            # Código para mostrar el listado de citas programadas para servicios y vacunación
            for Cita in Citas:
                # Mostrar los detalles de cada cita (servicios y vacunación)
                print(f"Cita {Citas.index(cita) + 1}:")
                for Clave, Valor in Cita.items():
                    print(f"{Clave}: {Valor}")
                print("-" * 20)

        elif reporte_opcion == "2":
            # Código para mostrar el listado de citas programadas
            for Cita in Citas:
                # Mostrar los detalles de cada cita
                print(f"Cita {Citas.index(Cita) + 1}:")
                for Clave, Valor in Cita.items():
                    print(f"{Clave}: {Valor}")
                print("-" * 20)

        elif reporte_opcion == "3":
            # Código para mostrar el listado de productos y/o servicios ofrecidos por semana o mes
            # Puedes agregar los datos necesarios para este reporte según lo que se haya registrado previamente
            print("Aún no hay datos para este reporte.")

        else:
            print("Opción de reporte inválida. Por favor, seleccione una opción válida.")

    elif Opcion == "7":
        print("Gracias por utilizar el sistema. Hasta luego.")

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")



