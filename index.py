from src.function.readFile import readFile
from src.menu.main import main

arquivos = readFile("src/data/dados_A618_D_2022-10-01_2023-12-31.csv")

main(arquivos)