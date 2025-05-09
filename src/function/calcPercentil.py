def calcPercentil(dados, percentil):
    lista_ordenada = sorted(dados, key=lambda x: x.temperatura)
    posicao = percentil * (len(lista_ordenada) + 1) / 100
    if posicao.is_integer():
        return lista_ordenada[int(posicao) - 1].temperatura
    else:
        posicao_inteira = int(posicao)
        fracao = posicao - posicao_inteira
        return lista_ordenada[posicao_inteira - 1].temperatura + fracao * (lista_ordenada[posicao_inteira].temperatura - lista_ordenada[posicao_inteira - 1].temperatura)