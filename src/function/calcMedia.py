def calcMedia(dados) -> float:
    total = 0
    for dado in dados:
        total += dado.temperatura
    return total / len(dados)