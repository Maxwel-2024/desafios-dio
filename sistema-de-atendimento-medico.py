n = int(input().strip())
pacientes = []
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

def prioridade(paciente):
    nome, idade, status = paciente
    # Urgente: prioridade 0, ordenar por idade descrescente
    # Idosos: prioridade 1, ordenar por idade descrescente
    # Demais: prioridade 2
    if status.lower() == "urgente":
        return (0, -idade)
    elif idade >= 60:
        return (1, -idade)
    else:
        return (2, 0)

pacientes.sort(key=prioridade)
nomes = [p[0] for p in pacientes]
print("Ordem de Atendimento:", ", ".join(nomes))