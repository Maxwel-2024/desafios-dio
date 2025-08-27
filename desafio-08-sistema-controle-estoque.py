# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input().strip()

# Verificação do produto
if produto in estoque:
    print("Produto disponível")
else:
    print("Produto esgotado")
