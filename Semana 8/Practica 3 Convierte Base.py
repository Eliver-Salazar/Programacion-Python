
def cambiobase(decimal, base):
    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        decimal = decimal // base
    return str(decimal) + conversion


numero = int(input('Ingrese un número a cambiar de base: '))
base = int(input('Ingrese la base: '))
print(cambiobase(numero, base))
