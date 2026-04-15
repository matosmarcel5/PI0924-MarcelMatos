contador = 0
soma = 0

while contador < 30:
    num = int(input("Digite um número (1-50): "))
    
    if 1 <= num <= 50 and num % 2 == 0:
        soma += num
        contador += 1
    else:
        print("Valor inválido! Deve ser par entre 1 e 50.")

media = soma / 30
print(f"Média: {media:.2f}")