from PIL import Image, ImageDraw, ImageFont
import csv

tags_csv_path:str = "Tags/FaceplateAutomaticTags.csv"

""" STEP-BY-STEP
- Abrir CSV

- iterar por cada linha do csv e lê coluna de equipamento salvando TAG numa varivel Auxiliar

- De acordo com o tipo do equipamento abre a pasta de faceplates correspondente
(Definir um padrao de nome para criar uma função geral)

- Abrir a imagem e salvar tamanho

- De acordo com o tamanho do faceplate importar Pos Central e TextSize
(Padronizar faceplates de mesmo tamanho e salvar suas configs num arquivo JSON)

- Escrever a TAG salva conforme as configs importadas e salvar numa pasta Faceplates/feitos
"""

#Try to open CSV

try:
    with open (tags_csv_path, mode='r', encoding='utf-8') as archive:
        
        #pass how to interpreter the csv
        read = csv.DictReader(archive, delimiter= ",")

        #iterate through every line in .csv archive, get equipaments and tag names
        for line in read:
            equipament:str = line.get("Equipamento", "")
            tag:str = line.get("TAG", "")
            
            #ignore void lines
            if (not equipament or not tag): continue

            print(f"Equipament: {equipament}")

            #CRIAR FUNÇÃO PARA RECEBER NOME EQUIPAMENTO E NAVEGAR ENTRE AS PASTAS E ABRIR FACEPLATES CORRETOS

        

except Exception as E:
    print("[ERROR]: Não foi possivel abrir o arquivo")
