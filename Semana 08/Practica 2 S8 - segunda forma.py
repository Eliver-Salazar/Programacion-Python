def convertir_a_binario(numero):
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    return binario

def convertir_a_octal(numero):
    octal = ""
    while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero = numero // 8
    return octal

def convertir_a_hexadecimal(numero):
    digitos_hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        digito = digitos_hex[residuo]
        hexadecimal = digito + hexadecimal
        numero = numero // 16
    return hexadecimal

def convertir_numero():
    numero = int(input("Ingrese un número decimal: "))
    binario = convertir_a_binario(numero)
    octal = convertir_a_octal(numero)
    hexadecimal = convertir_a_hexadecimal(numero)
    return binario, octal, hexadecimal

resultado = convertir_numero()
binario, octal, hexadecimal = resultado

print(f"El número en base binaria es:" ,binario)
print(f"El número en base octal es:", octal)
print(f"El número en base hexadecimal es:",hexadecimal)


