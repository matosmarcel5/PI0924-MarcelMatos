inicio = 0

while inicio <= 255:
    for i in range(inicio, min(inicio + 20, 256)):
        print(f"{i} -> {chr(i)}")
    
    inicio += 20
    
    opcao = input("Continuar? (s/n): ").lower()
    if opcao != 's':
        break