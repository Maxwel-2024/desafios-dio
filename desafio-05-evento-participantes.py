# Dicionário para agrupar participantes por tema
eventos = {}

n = int(input().strip())

for _ in range(n):
    linha = input().strip()
    participante, tema = [parte.strip() for parte in linha.split(",")]
    eventos.setdefault(tema, []).append(participante)

for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")