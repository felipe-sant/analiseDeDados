from src.function.calcMedia import calcMedia

def calcVariancia(dados) -> float:
    media = calcMedia(dados)
    soma = 0
    for dado in dados:
        soma += (dado.temperatura - media) ** 2
    variancia = soma / len(dados)
    return variancia