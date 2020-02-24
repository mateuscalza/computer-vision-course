import cv2

imagem = cv2.imread("./resources/quadrado.bmp", 0)

totalPixelsPretos = 0
totalPixelsBrancos = 0

for linha in range(0, imagem.shape[0]):
    for coluna in range(0, imagem.shape[1]):
        if imagem[linha, coluna] == 255:
            totalPixelsBrancos += 1
        else:
            totalPixelsPretos += 1

print("Pixels brancos:", totalPixelsBrancos)
print("Pixels pretos:", totalPixelsPretos)
