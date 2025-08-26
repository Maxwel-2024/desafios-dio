# Dicionário com usuários e senhas cadastrados
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",
}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# Validação do login
if usuario in usuarios and usuarios[usuario] == senha:
    print("Acesso permitido")
else:
    print("Usuário ou senha incorretos")
