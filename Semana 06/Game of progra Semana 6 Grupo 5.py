#INSTRUCCION IF-ELSE SEMANA 6 GAME OF PROGRA EJERCICIO 1


# Solicitud de articulo y precio

Articulo = input("Ingrese el artículo que desea comprar: ")
Precio = float(input("Ingrese el precio original del artículo: "))

#Descuentos

if Articulo == "Tarjeta Madre":
    Descuento = Precio * 0.05

elif Articulo == "Tarjeta de Video":
    Descuento = Precio * 0.08

elif Articulo == "Monitor":
    Descuento = Precio * 0.10

elif Articulo == "Teclado Gamer":
    Descuento = Precio * 0.15

else:
    Descuento = 0

#Precio a Pagar

PrecioPagar = Precio - Descuento

#Resultado
print("El precio a pagar después del descuento es:", PrecioPagar)
