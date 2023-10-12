
def crearArchivo () :
    file=open ("notasCurso. txt", "w")
    print ("El archivo está listo para grabar informacion!")
    file.close ()
    
def agregarInformacion () :
    nombreContacto=input ("Digite su nombre:")
    grupo=input ("Digite su número de grupo:")
    calificaciones=input ("Digite su calificación:")
    file=open ("notasCurso.txt", "a")
    file.write ("Nombre:" + nombreContacto)
    file.write("\n")
    file.write ("Número de grupo:" + grupo)
    file.write ("\n")
    file.write ("Calificación:" + calificaciones)
    file.write("\n\n")
    print ("\nLa información fue grabada correctamente!")
    file.close ()

def mostrarInformacion():
    file=open("notasCurso.txt", "r")
    mensaje=file.read()
    print(mensaje)
    file.close()

def mostrarMenu () :
    opc=0
    while(opc!=4) :
        opc=int (input ("**MENÚ PRINCIPAL** \n \n"+
        "1. Crear archivo\n"+
        "2. Agregar información\n"+
        "3. Mostar información\n"+
        "4. Salir del sistema\n\n"+
        "Digite su opción:" ))
        if (opc==1):
            crearArchivo()
        elif (opc==2) :
            agregarInformacion()
        elif(opc==3) :
            mostrarInformacion()
        elif(opc==4) :
            print("Muchas gracias, Que tengas bonito día")
            break
        else: 
            print ("Opcion: incorrecta!")

if __name__=="__main__":
    mostrarMenu()
