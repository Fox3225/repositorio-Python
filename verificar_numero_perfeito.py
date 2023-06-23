num = int(input("Digite um número: "))

sum_of_divisors = 0
for divisor in range(1, num):
    if num % divisor == 0:
        sum_of_divisors += divisor

if sum_of_divisors == num:
    print(num, "é um número perfeito.")
else:
    print(num, "não é um número perfeito.")
