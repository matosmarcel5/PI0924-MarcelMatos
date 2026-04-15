n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))

media = (n1*2 + n2*3 + n3*5) / 10

print(f"Média: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")