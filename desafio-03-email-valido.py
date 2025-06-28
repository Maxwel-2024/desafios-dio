email = input().strip()

dominios_validos = ["gmail.com", "outlook.com"]
# Verificas apenas esses dominios válidos
if (
    "@" in email and
    " " not in email and
    not email.startswith("@") and
    not email.endswith("@")
):
    usuario, sep, dominio = email.partition("@")
    if dominio in dominios_validos and usuario:
        print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")