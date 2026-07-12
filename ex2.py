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
        if palpite == numero:
            print(f"\nParabéns! Você acertou em {tentativas} tentativa(s).")
            break

        elif palpite > numero:
            print("Muito alto!")

        else:
            print("Muito baixo!")

        print(f"Tentativas restantes: {7 - tentativas}")

    else:
        print("\nVocê perdeu!")
        print(f"O número era {numero}.")

    print("Histórico de tentativas:", historico)

    jogar = input("\nDeseja jogar novamente? (s/n): ").lower()

    if jogar != "s":
        print("Obrigado por jogar!")
        break