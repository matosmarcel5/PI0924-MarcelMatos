notas = []

for i in range(10):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / 10

acima_media = sum(1 for n in notas if n >= media)

print(f"Média: {media:.2f}")
print(f"Alunos >= média: {acima_media}")