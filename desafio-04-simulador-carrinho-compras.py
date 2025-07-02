# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# O uso de for _ in range(n): é uma convenção em Python quando você quer repetir uma ação
#  n vezes mas não precisa usar o valor do índice dentro do loop.
# Ou seja sem declarar uma variável de controle.
for _ in range(n):
    linha = input().strip() 

    # Esse método salva a posição do último espaço de toda a string digitada em linha.
    # Ou seja, se a linha for "Arroz Integral 10.50" a posição do espaço será o índice 14.
    # Contando do zero, ou seja, o primeiro caractere "A" é o índice 0.
    posicao_espaco = linha.rfind(" ")
    
    # Pega tudo antes do indice do ultimo espaço e adiciona a variável item.
    item = linha[:posicao_espaco]
    # Pega tudo depois do indice (14) soma + 1 (15), até o final da string
    # adiciona a variável preco.
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