pares = []
impares = []

num = 1
while len(pares) < 30 or len(impares) < 30:
    if num % 2 == 0 and len(pares) < 30:
        pares.append(num)
    elif num % 2 != 0 and len(impares) < 30:
        impares.append(num)
    num += 1

print("Pares:", pares)
print("Ímpares:", impares)