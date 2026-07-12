total_produtos = 0
soma_precos = 0
mais_caro = ""
preco_mais_caro = 0
acima_100 = 0

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    preco = float(input("Digite o preço do produto: R$ "))

    total_produtos += 1

    soma_precos += preco

    if total_produtos == 1 or preco > preco_mais_caro:
        preco_mais_caro = preco
        mais_caro = nome

    if preco > 100:
        acima_100 += 1
        print("\n===== RELATÓRIO =====")

if total_produtos > 0:
    media = soma_precos / total_produtos

    print(f"Total de produtos: {total_produtos}")
    print(f"Produto mais caro: {mais_caro} (R$ {preco_mais_caro:.2f})")
    print(f"Média dos preços: R$ {media:.2f}")
    print(f"Produtos acima de R$100: {acima_100}")
else:
    print("Nenhum produto foi cadastrado.")