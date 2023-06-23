import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

    while guess != number:
        guess = int(input("Digite o seu palpite: "))
        attempts += 1

        if guess < number:
            print("Está frio! O número correto é maior.")
        elif guess > number:
            print("Está quente! O número correto é menor.")

    print(f"Parabéns! Você acertou o número {number} em {attempts} tentativas.")

guess_number()
