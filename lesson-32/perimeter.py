import cv2

imagem = cv2.imread("./resources/quadrado.bmp", 0)

img_bordas = cv2.Canny(imagem, 100, 200)

cv2.imshow("Original", imagem)
cv2.imshow("Bordas", img_bordas)

totalPixelsBrancos = 0
for linha in range(0, img_bordas.shape[0]):
    for coluna in range(0, img_bordas.shape[1]):
        if img_bordas[linha, coluna] == 255:
            totalPixelsBrancos += 1

print("Perímetro (cálculo manual):", totalPixelsBrancos)

# Obtendo os contornos dos objetos na imagem
modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE
img, contornos, hierarquia = cv2.findContours(imagem, modo, metodo)

# Obtendo os contornos do primeiro objeto segmentado
objeto = contornos[0]

# Obtendo a area do objeto segmentado
perimetro = cv2.arcLength(objeto, True)
print("Perímetro (OpenCV):", perimetro)

cv2.waitKey(0)
cv2.destroyAllWindows()
