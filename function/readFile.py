from model.Temperatura import Temperatura

def readFile(file_path) -> list:
    dados = []
    
    with open(file_path, 'r') as file:
        arquivo = file.read().split("\n")
        for linha in arquivo[1:-2]:
            dado = linha.split(";")
            obj = Temperatura(dado[0], dado[1])
            dados.append(obj)
    
    return dados