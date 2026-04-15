soma = 0

for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    soma += nota

media = soma / 10
print(f"Média: {media:.2f}")