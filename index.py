from function.readFile import readFile
from menu.main import main

arquivos = readFile("data/dados_A618_D_2022-10-01_2023-12-31.csv")

main(arquivos)