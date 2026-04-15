primos = []
num = 2

while len(primos) < 10:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    
    if primo:
        primos.append(num)
    
    num += 1

print(primos)