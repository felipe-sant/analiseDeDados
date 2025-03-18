def readFile(file_path):
    dados = []
    
    with open(file_path, 'r') as file:
        arquivo = file.read().split("\n")
        for linha in arquivo[1:-2]:
            dado = linha.split(";")
            dado = dado[0:-1]
            dados.append(dado)
    
    return dados