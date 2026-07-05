from PIL import Image, ImageDraw, ImageFont

""" STEP-BY-STEP
- Baixa CSV

- iterar por cada linha do csv e lê coluna de equipamento salvando TAG numa varivel Auxiliar

- De acordo com o tipo do equipamento abre a pasta de faceplates correspondente
(Definir um padrao de nome para criar uma função geral)

- Abrir a imagem e salvar tamanho

- De acordo com o tamanho do faceplate importar Pos Central e TextSize
(Padronizar faceplates de mesmo tamanho e salvar suas configs num arquivo JSON)

- Escrever a TAG salva conforme as configs importadas e salvar numa pasta Faceplates/feitos
"""

# 1. Carrega a imagem base
img = Image.open("rFaceplates/ELECTRICAL/ATS ALARMS.png")
draw = ImageDraw.Draw(img)

# 2. Configura todos os paramentros de posição de texto no faceplate
width, height = img.size
textSize = 10
CenterX = width * 0.5
CenterY = height * 0.025

# 3. Define a posição Central do Retangulo(X, Y) e a cor (RGB)
posicao1 = (CenterX, CenterY)
posicao2 = (CenterX, CenterY + textSize)
cor = (255, 255, 255) # Branco

# 4. Insere o texto centralizado
draw.text(posicao1, "Texto de Teste", fill=cor, anchor="mm" )  #, font=fonte, fill=cor)
draw.text(posicao2, "Texto de Teste maior", fill=cor, anchor="mm" )  #, font=fonte, fill=cor)

# 5. Salva o resultado
img.save("imagem_editada.jpg")

