from src.function.calcQuartil import calcQuartil

def calcOutliers(dados) -> list:
    Q1 = calcQuartil(dados, 1)
    Q3 = calcQuartil(dados, 3)
    IQR = Q3 - Q1
    limiteInferior = Q1 - 1.5 * IQR
    limiteSuperior = Q3 + 1.5 * IQR
    
    outliers = []
    
    for dado in dados:
        if dado.temperatura < limiteInferior or dado.temperatura > limiteSuperior:
            outliers.append(dado)
        
    return outliers