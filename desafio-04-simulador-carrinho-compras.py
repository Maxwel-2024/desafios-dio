# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho mas de forma que o nome do produto pode conter espaços
# EX: Se você digitar 3 para n, ele vai pedir para você digitar 3 linhas (uma para cada item do carrinho).
# Cada linha deve conter o nome do produto e o preço, separados por espaço.
for _ in range(n):
    linha = input().strip() 

    # Esse método encontra a última ocorrência de espaço na string, que é onde o preço começa.
    # Pega tudo antes do espaço como o nome do produto e tudo depois como o preço.
    # Isso permite que o nome do produto contenha espaços.
    # Por isso usamos o rfind, após a variável linha para encontrar o último espaço.
    posicao_espaco = linha.rfind(" ")
    
    # Pega tudo antes do espaço e adiciona a variável item.
    item = linha[:posicao_espaco]
    # Pega tudo depois do espaço e converter para float, adiciona a variável preco.
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho está criando na variável carrinho a lista de tuplas
    # Onde cada tupla contém o nome do item e o preço.
    carrinho.append((item, preco))
    total += preco

# **Exibe os itens do carrinho, no caso esse foi a nossa alteração no desafio**
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Exibe o total da compra
print(f"Total: R${total:.2f}")