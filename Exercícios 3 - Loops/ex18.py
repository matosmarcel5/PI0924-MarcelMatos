limite = int(input("Até que número quer verificar? "))
contador = 0

for num in range(1, limite + 1):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    
    if soma == num:
        print(f"{num} é perfeito")
        contador += 1

print("Quantidade de números perfeitos:", contador)