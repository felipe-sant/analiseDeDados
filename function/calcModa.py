from collections import Counter

def calcModa(dados) -> float:
    contagem = Counter(dados.temperatura for dados in dados)
    moda = [k for k, v in contagem.items() if v == contagem.most_common(1)[0][1]]
    return moda[0] if moda else None