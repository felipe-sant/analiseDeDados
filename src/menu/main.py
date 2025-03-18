from src.utils.formatText import formatarTexto_negrito, formatarTexto_tachado
from src.function.calcModa import calcModa
from src.function.calcMedia import calcMedia
from src.function.calcMediana import calcMediana
from src.function.calcVariancia import calcVariancia
from src.function.calcDesvioPadrao import calcDesvioPadrao
from src.function.calcQuartil import calcQuartil

def main(dados):
    while True:
        
        print()
        print(formatarTexto_negrito("Menu Principal"))
        print("=="*20)
        print("1 | Media, moda e mediana")
        print("2 | Desvio padrão e variância")
        print("3 | 1º, 2º e 3º quartil")
        print(formatarTexto_tachado("4 | 5º e 95º percentil"))
        print(formatarTexto_tachado("5 | Outliers"))
        print(formatarTexto_tachado("6 | Gráfico de Boxplot"))
        print("7 | Mostrar todos os dados")
        print("--"*20)
        print("0 | Sair")
        print("=="*20)
        print()
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            print()
            print("Moda:", calcModa(dados))
            print("Média:", calcMedia(dados))	
            print("Mediana:", calcMediana(dados))
            print()
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            print()
            print("Variancia:", calcVariancia(dados))
            print("Desvio Padrão:", calcDesvioPadrao(dados))
            print()
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            print()
            print("1º Quartil:", calcQuartil(dados, 1))
            print("2º Quartil:", calcQuartil(dados, 2))
            print("3º Quartil:", calcQuartil(dados, 3))
            print()
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            print("Opção 4")
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            print("Opção 5")
            input("Pressione Enter para continuar...")
        elif opcao == "6":
            print("Opção 6")
            input("Pressione Enter para continuar...")
        elif opcao == "7":
            for dado in dados:
                print(dado)
            input("\nPressione Enter para continuar...")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("\nOpção inválida!\n")
            input("Pressione Enter para continuar...")