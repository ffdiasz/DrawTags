import csv
import FaceplateDraw
from configs import *

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

configPaths = ConfigManager()

try:
    with open (configPaths.csvPath, mode='r', encoding='utf-8') as archive:
        
        #pass how to interpreter the csv
        read = csv.DictReader(archive, delimiter= ",")

        #iterate through every line in .csv archive, get equipaments and tag names
        for line in read:
            equipament:str = line.get("Equipamento", "")
            tag:str = line.get("TAG", "")
            description:str = line.get("Descricao", "")
            
            #ignore void lines
            if (not equipament or not tag): continue

            #Write tags on the faceplates and save
            FaceplateDraw.DrawTag(equipament, tag, description)

except Exception as E:
    print(f"[ERROR]: Não foi possivel abrir o arquivo \nerror: {E}")
