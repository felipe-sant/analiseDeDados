from function.readFile import readFile

arquivos = readFile("data/dados_A618_D_2022-10-01_2023-12-31.csv")

for arquivo in arquivos:
    print(arquivo)