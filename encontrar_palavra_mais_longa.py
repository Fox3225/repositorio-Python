words = []
while True:
    word = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if word.lower() == "sair":
        break
    words.append(word)

if len(words) > 0:
    longest_word = max(words, key=len)
    print("A palavra mais longa é:", longest_word)
else:
    print("Nenhuma palavra foi digitada.")
