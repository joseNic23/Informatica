intentos = 0
monto = 5000
while intentos < 3:
    pin = input("Ingrese su PIN: ")
    if pin.isdigit() and len(pin) == 4:
        print("PIN aceptado.")
        monto = int(input("Ingrese el monto a retirar: "))  
        if monto <= 5000:
            print("Monto retirado:", monto)
            saldo = 5000 - monto
            print("Saldo restante:", saldo)
        else:
            print("Monto excede el saldo disponible.")  
        break
    else:
        intentos += 1
        print("PIN incorrecto. Intentos restantes:", 3 - intentos)  
else:
    print("PIN incorrecto targeta bloqueada")
