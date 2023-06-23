num = int(input("Digite um número: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("O fatorial de", num, "é", factorial)
