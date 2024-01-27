def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal

def binario_a_octal(binario):
    decimal = int(binario, 2)
    octal = oct(decimal)
    return octal

def binario_a_hexadecimal(binario):
    decimal = int(binario, 2)
    hexadecimal = hex(decimal)
    return hexadecimal

def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

def decimal_a_octal(decimal):
    octal = oct(decimal)
    return octal

def decimal_a_hexadecimal(decimal):
    hexadecimal = hex(decimal)
    return hexadecimal

def octal_a_binario(octal):
    decimal = int(octal, 8)
    binario = bin(decimal)[2:]
    return binario

def octal_a_decimal(octal):
    decimal = int(octal, 8)
    return decimal

def octal_a_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)
    return hexadecimal

def hexadecimal_a_binario(hexadecimal):
    decimal = int(hexadecimal, 16)
    binario = bin(decimal)[2:]
    return binario

def hexadecimal_a_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

def hexadecimal_a_octal(hexadecimal):
    decimal = int(hexadecimal, 16)
    octal = oct(decimal)
    return octal

def menu():
    while True:
        print("\nMenu")
        print("1.Binario a decimal")
        print("2.Binario a octal")
        print("3.Binario a hexadecimal")
        print("4.Decimal a binario")
        print("5.Decimal a octal")
        print("6.Decimal a hexadecimal")
        print("7.Octal a binario")
        print("8.Octal a decimal")
        print("9.Octal a hexadecimal")
        print("10.Hexadecimal a binario")
        print("11.Hexadecimal a binario")
        print("12.Hexadecimal a binario")
        print("0.Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            numero_binario = input("Ingresa el número binario: ")
            resultado_decimal = binario_a_decimal(numero_binario)
            print(f"El numero binario {numero_binario} en decimal es: {resultado_decimal}")

        elif opcion == "2":
            numero_binario = input("Ingrese el numero binario: ")
            resultado_octal = binario_a_octal(numero_binario)
            print(f"El numero binario {numero_binario} en octal es: {resultado_octal}")

        elif opcion == "3":
            numero_binario = input("Ingresa el número binario: ")
            resultado_hexadecimal = binario_a_hexadecimal(numero_binario)
            print(f"El número binario {numero_binario} en hexadecimal es: {resultado_hexadecimal}")

        elif opcion == "4":
            numero_decimal = int(input("Ingresa el número decimal: "))
            resultado_binario = decimal_a_binario(numero_decimal)
            print(f"El número decimal {numero_decimal} en binario es: {resultado_binario}")

        elif opcion == "5":
            numero_decimal = int(input("Ingresa el número decimal: "))
            resultado_octal = decimal_a_octal(numero_decimal)
            print(f"El número decimal {numero_decimal} en octal es: {resultado_octal}")

        elif opcion == "6":
            numero_decimal = int(input("Ingresa el número decimal: "))
            resultado_hexadecimal = decimal_a_hexadecimal(numero_decimal)
            print(f"El número decimal {numero_decimal} en hexadecimal es: {resultado_hexadecimal}")

        elif opcion == "7":
            numero_octal = input("Ingresa el número octal: ")
            resultado_binario = octal_a_binario(numero_octal)
            print(f"El número octal {numero_octal} en binario es: {resultado_binario}")

        elif opcion == "8":
            numero_octal = input("Ingresa el número octal: ")
            resultado_decimal = octal_a_decimal(numero_octal)
            print(f"El número octal {numero_octal} en decimal es: {resultado_decimal}")

        elif opcion == "9":
            numero_octal = input("Ingresa el número octal: ")
            resultado_hexadecimal = octal_a_hexadecimal(numero_octal)
            print(f"El número octal {numero_octal} en hexadecimal es: {resultado_hexadecimal}")

        elif opcion == "10":
            numero_hexadecimal = input("Ingresa el número hexadecimal: ")
            resultado_binario = hexadecimal_a_binario(numero_hexadecimal)
            print(f"El número hexadecimal {numero_hexadecimal} en binario es: {resultado_binario}")

        elif opcion == "11":
            numero_hexadecimal = input("Ingresa el número hexadecimal: ")
            resultado_decimal = hexadecimal_a_decimal(numero_hexadecimal)
            print(f"El número hexadecimal {numero_hexadecimal} en decimal es: {resultado_decimal}")

        elif opcion == "12":
            numero_hexadecimal = input("Ingresa el número hexadecimal: ")
            resultado_octal = hexadecimal_a_octal(numero_hexadecimal)
            print(f"El número hexadecimal {numero_hexadecimal} en octal es: {resultado_octal}")

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida")


menu()