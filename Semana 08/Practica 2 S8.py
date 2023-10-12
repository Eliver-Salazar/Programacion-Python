def convertir_binario(numero):
    binario = bin(numero)
    return binario[2:]

def convertir_octal(numero):
    octal = oct(numero)
    return octal[2:]

def convertir_hexadecimal(numero):
    hexadecimal = hex(numero)
    return hexadecimal[2:]

def mostrar_numero(numero, base):
    if base == 2:
        print(f"El número en base binaria es: {convertir_binario(numero)}")
    elif base == 8:
        print(f"El número en base octal es: {convertir_octal(numero)}")
    elif base == 16:
        print(f"El número en base hexadecimal es: {convertir_hexadecimal(numero)}")
    else:
        print("Base no válida. Ingrese 2 para binario, 8 para octal o 16 para hexadecimal.")

numero = int(input("Ingrese un número: "))

mostrar_numero(numero, 2)
mostrar_numero(numero, 8)
mostrar_numero(numero, 16)
