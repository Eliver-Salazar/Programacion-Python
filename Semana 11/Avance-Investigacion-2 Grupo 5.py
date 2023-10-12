def main():
    print("\n*************** CLÍNICA DE MASCOTAS GARDEN ***************\n");    

    usuario = "";
    contrasena= "";
    opcion = 0;
    clientes=[];
    vacunacion=[];

    while usuario != "admin" or contrasena != "Adm115":
        usuario = str(input("Por favor digite su nombre de usuario\n"));
        contrasena = str(input("Por favor digite su contraseña: "));
        if usuario == "admin" and contrasena == "Adm115":
            print("\nInicio de sesión exitoso.");
        else:
            print("\nError, intente nuevamente.\n");

    while opcion != 5:
        print("\n   --------- Menú --------- ");
        print("|  1. Registrar cliente     |");
        print("|  2. Módulo vacunación     |");
        print("|  3. Módulo de facturación |");
        print("|  4. Módulo de reportes    |");
        print("|  5. Salir                 |");
        print("   ------------------------");
        opcion = int(input("Por favor seleccione una opción: "));

        if opcion == 1:
            idUsuario = len(clientes) + 1;
            clientes.append(RegistroCliente(idUsuario));
        elif opcion == 2:
            nuevaVacuna = ModuloVacunacion(clientes);
            if nuevaVacuna != None:
                vacunacion.append(nuevaVacuna);            
        elif opcion == 3:
            ModuloFacturacion();
        elif opcion == 4:
            ModuloReportes(clientes, vacunacion);
        elif opcion == 5:
            print("\n ******* Salida ******* ");
            print("\nGracias por utilizar el sistema.");   

def RegistroCliente(idUsuario):    
    print("\n ******* Registro Cliente ******* ");

    print("\nDATOS DUEÑO");

    nombreDueño = input("Por favor digite el nombre completo del dueño: ");
    cedulaDueño = input("Por favor digite la cédula del dueño: ");
    telefonoDueño = input("Por favor digite el número de teléfono del dueño: ");
    correoDueño = input("Por favor digite el correo del dueño: ");
    direccionDueño = input("Por favor digite la dirección del dueño: ");

    print("\nDATOS MASCOTA");

    nombreMascota = input("Por favor digite el nombre de la mascota: ");
    razaMascota = input("Por favor digite la raza de la mascota: ");
    fechaNacimiento = input("Por favor digite la fecha de nacimiento de la mascota (DD/MM/AAAA): ");
    sexoMascota = input("Por favor digite el sexo de la mascota (Macho/Hembra): ");
    pesoMascota = input("Por favor digite el peso de la mascota (Kg): ");
    caracteristicasMascota = input("Por favor digite las características de la mascota: ");
    alimentoMascota = input("Por favor digite el alimento que consume la mascota: ");
    observacionesMascota = input("Por favor digite las observaciones generales de la mascota: ");

    print("\nDATOS CITA");

    turnoCita = input("Por favor digite el turno de la cita (Mañana/Tarde/Noche): ");
    horarioCita = input("Por favor digite el horario de la cita (00:00)am/pm: ");
    fechaCita = input("Por favor digite la fecha de la cita (DD/MM/AAAA): ");
    especialidadCita = input("Por favor digite la especialidad o tratamiento requerido: ");
    medicoAsignado = input("Por favor digite el nombre del médico asignado: ");

    usuario = {
        "idUsuario": idUsuario,
        "nombreDueño": nombreDueño,
        "cedulaDueño": cedulaDueño,
        "telefonoDueño": telefonoDueño,
        "correoDueño": correoDueño,
        "direccionDueño": direccionDueño,
        "nombreMascota": nombreMascota,
        "razaMascota": razaMascota,
        "fechaNacimiento": fechaNacimiento,
        "sexoMascota": sexoMascota,
        "pesoMascota": pesoMascota,
        "caracteristicasMascota": caracteristicasMascota,
        "alimentoMascota": alimentoMascota,
        "observacionesMascota": observacionesMascota,
        "turnoCita": turnoCita,
        "horarioCita": horarioCita,
        "fechaCita": fechaCita,
        "especialidadCita": especialidadCita,
        "medicoAsignado": medicoAsignado
    }
    print("\n ******* Registro Exitoso ******* \n"); 
    print("\nRegresando al menú...");   
    input("Presione enter continuar... ");  
    return usuario;

def ModuloVacunacion(clientes):
    reiniciar = 0;
    while reiniciar != 1:
        print("\n ******* Módulo Vacunación ******* \n");
        if len(clientes) != 0:
            mascotaAVacunar = str(input("Digite el nombre de la mascota a la que desea agendar una vacunación: "));
            mascotaEncontrada="";
            nombreDueno="";
            idUsuario="";

            for i in clientes:
                mascota = i.get('nombreMascota');
                if mascota == mascotaAVacunar:
                    idUsuario = i.get('idUsuario');
                    nombreDueno = i.get('nombreDueño');

                    print("\n *** Success *** ");            
                    print("\n¡Mascota encontrada en la base de datos!\n");
                    print(f"Nombre Dueño: {nombreDueno}");
                    print(f"Nombre Mascota: {mascota}");
                    print(f"Descripción Mascota: {i.get('caracteristicasMascota')}\n");             
                    mascotaEncontrada = mascota;
            
            if len(mascotaEncontrada) >= 1:
                medicamento = str(input("Digite el medicamento a aplicar a la mascota: "));
                fechaColocacion = str(input("Digite la fecha de colocación de la vacuna (DD/MM/AAAA): "));
                dosis = int(input("Digite la cantidad de dosis a aplicar: "));
                proximaFecha = str(input("Digite la proxima fecha de colocación de la vacuna (DD/MM/AAAA): "));
            
                nuevaVacunacion = {
                    "idUsuario": idUsuario,
                    "idVacunacion": idUsuario,
                    "nombreDueño": nombreDueno,
                    "nombreMascota": mascota,
                    "medicamento": medicamento,
                    "fechaColocacion": fechaColocacion,
                    "dosis": dosis,
                    "proximaFecha": proximaFecha
                };

                print("\n ******* Registro De Vacunación Exitoso ******* \n"); 
                print("\nRegresando al menú...");   
                input("Presione enter continuar... ");  
                return nuevaVacunacion;

            else:
                print("\n *** Error *** ");
                print("\nMascota no encontrada en la base de datos");
                opcion = int(input("\n¿Desea registrarla?\n[1] Registrarla\n[2] Intentar de nuevo\nPor favor digite el numero que desea "));
                if opcion == 1:
                    print("\nRegresando al menú...");   
                    input("Presione enter continuar... ");  
                    reiniciar = 1;
                    return None;
                else:
                    print("\nRegresando al inicio...");
                    input("Presione enter continuar... ");      
    
        else:
            print("\nNo hay clientes ó mascotas a las cuales registrar una vacunación");
            print("Por favor registre un cliente");
            print("\nRegresando al menú...");   
            input("Presione enter continuar... ");

def ModuloFacturacion():
    print("\n ******* Modulo Facturación ******* \n");   

    nombreCliente = input("Por favor digite el nombre completo del cliente: ");
    descripcionServicio = input("Por favor digite la descripción del servicio: ");
    cantidadServicio = int(input("Por favor digite la cantidad de servicios brindados: "));
    precioServicio = int(input("Por favor digite el precio del servicio brindado: "));
    descuento = int(input("Por favor digite el descuento (Numero porcentaje): "));
    iva = int(input("Por favor digite el IVA (Numero porcentaje): "));
    subTotal = precioServicio * cantidadServicio;
    descuentoAplicable = subTotal * (descuento / 100);
    ivaAplicable = subTotal * (iva / 100);
    totalGeneral = (subTotal - descuentoAplicable) -ivaAplicable;

    print("\n   ------------ FACTURA ------------ ");
    print("|");
    print(f"|  Cliente: {nombreCliente}");
    print(f"|  Descripción: {descripcionServicio}");
    print(f"|  Cantidad: {cantidadServicio}");
    print(f"|  Precio servicio: {precioServicio}");
    print(f"|  Descuento: {descuento}%");
    print(f"|  IVA: {iva}%");
    print(f"|  Subtotal: {subTotal}");
    print(f"|  Total General: {totalGeneral}");
    print("   ---------------------------------");

    print("\n ******* Factura generada ******* "); 
    print("\nRegresando al menú...");   
    input("Presione enter continuar... ");

def ModuloReportes(clientes, vacunacion):
    opcion = 0;
    while opcion !=5:
        print("\n ******* Módulo Reportes ******* "); 
        print("\n   ------------- Menú ----------------   ");
        print("|  1. Mostrar base de datos de clientes   |");
        print("|  2. Mostrar base de datos de vacunación |");
        print("|  3. Listado de servicios brindados      |");
        print("|  4. Listado de citas programadas        |");
        print("|  5. Salir                               |");
        print("   -------------------------------------   ");
        opcion = int(input("Por favor seleccione una opción: "));

        if opcion == 1: 
            print("\n ******* Base De Datos de Clientes ******* \n");
            if len(clientes) >= 1:
                print("Listado de clientes");
                for i in clientes:
                    print(i);
                input("Presione enter continuar... "); 
            else: 
                print("No hay clientes registrados");
                input("Presione enter continuar... "); 
        elif opcion == 2:
            print("\n ******* Base De Datos de Vacunación ******* \n");
            if len(vacunacion) >= 1:
                for i in vacunacion:
                    print(f"\nVacunación Registrada {i}");
                input("\nPresione enter continuar... "); 
            else: 
                print("No hay vacunaciones registradas");
                input("Presione enter continuar... "); 
        elif opcion == 3:
            print(f"\nCantidad de clientes registrados {len(clientes)}");
            print(f"Cantidad de vacunaciones registradas: {len(vacunacion)}");
            input("\nPresione enter continuar... ");
        elif opcion == 4:
            print(f"\nCantidad de citas registradas: {len(clientes)}");
            print("\n***** CITAS *****\n");
            print("Citas registradas:");
            citas = citasProgramadas(clientes);
            for i in citas:
                print(i);
            input("\nPresione enter continuar... "); 
        elif opcion == 5:
            print("\nRegresando al menú...");
            input("Presione enter continuar... "); 

def citasProgramadas(clientes):
    citasProgramada = [];
    if len(clientes):        
        for cliente in clientes:
            nuevaCita = {
                "idCita": cliente.get('idUsuario'),
                "nombreMascota": cliente.get('nombreMascota'),
                "nombreDueño": cliente.get('nombreDueño'),
                "turnoCita": cliente.get('turnoCita'),
                "horarioCita": cliente.get('horarioCita'),
                "fechaCita": cliente.get('fechaCita'),
                "especialidadCita": cliente.get('especialidadCita'),
                "medicoAsignado": cliente.get('medicoAsignado')
            }
            citasProgramada.append(nuevaCita);
    return citasProgramada;
            
if __name__ == "__main__":
    main()
