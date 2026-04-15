num = int(input("Digite um número: "))

soma = 0
sub = 0
mult = 1
div = num
contador = 0

for i in range(1, num):
    soma += i
    sub -= i
    mult *= i
    if i != 0:
        div /= i
    contador += 4 
    
print("Subtração:", sub)
print("Multiplicação:", mult)
print("Divisão:", div)
print("Total de operações:", contador)