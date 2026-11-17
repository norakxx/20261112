from clases import Client, BankAccount

# Menu
# crear un cliente
# crear una cuenta bancaria para ese cliente
# ingresar dinero en la cuenta
# sacar dinero de la cuenta

activo = True

while activo:
    print("Bienvenido al sistema bancario")
    print("1. Crear un cliente")
    print("2. Crear una cuenta bancaria para un cliente")
    print("3. Ingresar dinero en la cuenta")
    print("4. Sacar dinero de la cuenta")
    print("5. Transferir dinero entre cuentas")
    print("X. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "X":
        activo = False
        print("Chao pescao")

    elif opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        pinvalido = False
        while not(pinvalido):
            pin1 = input("Ingrese el PIN del cliente: ")
            pin2 = input("Ingrese el PIN de nuevo para confirmarlo: ")
            if pin1 == pin2:
                pinvalido = True
                pin = pin1
            else:
                print("Los PINs no coinciden. Intente de nuevo.")
        cliente = Client(nombre, apellido, pin)
        print(f"Cliente creado: {cliente}")

    elif opcion == "2":
        numero_cuenta = 0
        #elegir un cliente
        #crear una cuenta bancaria para ese cliente
    
    elif opcion == "4":
        #elegir una cuenta bancaria
        #buscar el cliente en la lista de clientes
        #elegir una cuenta bancaria del cliente
        #sacar dinero de la cuenta
        pass
    elif opcion == "5":
        cuenta_origen = input("Ingrese el número de cuenta de origen: ")
        cuenta_destino = input("Ingrese el número de cuenta de destino: ")
        prueba_pin = input("Ingrese el PIN de la cuenta de origen: ")
        intentos_pin = 0
        max_intentos = 3
        pin_correcto = False
        while not(pin_correcto) and intentos_pin < max_intentos:
            if not(prueba_pin == cuenta_origen.clientpin):
                print("PIN incorrecto. No se puede realizar la transferencia.")
            else:
                pin_correcto = True

        #elegir una cuenta bancaria
        #buscar el cliente en la lista de clientes
        #elegir una cuenta bancaria del cliente
        #transferir dinero entre cuentas
        pass