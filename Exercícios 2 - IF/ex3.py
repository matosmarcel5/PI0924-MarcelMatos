num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

crescente = sorted([num1, num2])
decrescente = sorted([num1, num2], reverse=True)

print("Crescente:", crescente)
print("Decrescente:", decrescente)