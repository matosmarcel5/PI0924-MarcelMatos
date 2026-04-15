saldo = float(input("Saldo: "))
cheque = float(input("Cheque: "))

if cheque > saldo:
    print("Cheque não pode ser descontado")
else:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo}")