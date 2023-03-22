num1 = float(input("Digite um numero"))
num2 = float(input("Digite outro numero"))
mdo = int(input("Digite 1 para soma, 2 para multiplicação, 3 para divisão"))
print('')
if mdo == 1:
    print(num1 + num2)
elif mdo == 2:
    print(num1 * num2)
elif mdo == 3:
    print(num1 / num2)
else:
    print("opção não identificada")
