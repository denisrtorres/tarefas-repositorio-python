import random

while True:
    numero = random.randint(1, 100)
    tentativas = 0
    historico = []

    print("\n===== JOGO DA ADIVINHAÇÃO =====")
    print("Tente adivinhar um número entre 1 e 100.")
    print("Você tem 7 tentativas.")

    while tentativas < 7:

        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        tentativas += 1
        historico.append(palpite)