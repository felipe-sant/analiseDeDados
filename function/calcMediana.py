def calcMediana(dados):
    lista_ordenada = sorted(dados, key=lambda x: x.temperatura)
    n = len(lista_ordenada)
    medio = n // 2
    
    if n % 2 == 0:
        return lista_ordenada[medio - 1].temperatura + lista_ordenada[medio].temperatura / 2
    else:
        return lista_ordenada[medio].temperatura