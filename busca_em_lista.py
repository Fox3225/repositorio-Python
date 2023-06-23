numeros = [2, 4, 6, 8, 10]
procurar_valor = 7

for numero in numeros:
    if numero == procurar_valor:
        print("numero encontrado!")
        break
else:
    print("numero não encontrado")
