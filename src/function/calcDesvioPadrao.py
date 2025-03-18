from src.function.calcVariancia import calcVariancia

def calcDesvioPadrao(dados) -> float:
    return calcVariancia(dados) ** 0.5