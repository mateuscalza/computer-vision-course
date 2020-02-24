import cv2

imagem = cv2.imread("./resources/quadrado.bmp", 0)

tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagem, 127, 255, tipo)

# Obtendo os contornos dos objetos na imagem
modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE
img, contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

# Obtendo os contornos do primeiro objeto segmentado
objeto = contornos[0]

# Obtendo a area do objeto segmentado
area = cv2.contourArea(objeto)
print("Área:", area, "pixels brancos")
