def main(arquivos):
    while True:
        
        print()
        print("Menu Principal")
        print("=="*20)
        print("1 | Media, moda e mediana")
        print("2 | Variancia e desvio padrão")
        print("3 | 1º, 2º e 3º quartil")
        print("4 | 5º e 95º percentil")
        print("5 | Outliers")
        print("6 | Gráfico de Boxplot")
        print("7 | Mostrar todos os dados")
        print("--"*20)
        print("0 | Sair")
        print("=="*20)
        print()
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            print("Opção 1")
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            print("Opção 2")
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            print("Opção 3")
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
            for arquivo in arquivos:
                print(arquivo)
            input("\nPressione Enter para continuar...")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("\nOpção inválida!\n")
            input("Pressione Enter para continuar...")