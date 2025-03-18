import matplotlib.pyplot as plt

def criarBoxplot(dados):
    boxplotDados = []
    
    for dado in dados:
        boxplotDados.append(dado.temperatura)
    
    plt.boxplot(boxplotDados)
    plt.title("Temperatura")
    plt.ylabel('Valores')
    plt.show()