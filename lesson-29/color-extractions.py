import cv2
import statistics

imgBinaria = cv2.imread("./resources/tampa-pb.bmp", 0)
imgTonsDeCinza = cv2.imread("./resources/tampa-cinza.png", 0)
imgRGB = cv2.imread("./resources/tampa-rgb.png")

rolBinaria = imgBinaria.ravel()
rolTonsDeCinza = imgTonsDeCinza.ravel()
rolRGB = imgRGB.ravel()

valorMedioBinaria = cv2.mean(imgBinaria)
valorMedioCinza = cv2.mean(imgTonsDeCinza)
valorMedioRGB = cv2.mean(imgRGB)

print("Média imagem binária - OpenCV:", valorMedioBinaria, "- Statistics:", statistics.mean(rolBinaria))
print("Média imagem tons de cinza - OpenCV:", valorMedioCinza, "- Statistics:", statistics.mean(valorMedioCinza))
print("Média imagem RGB - OpenCV:", valorMedioRGB, "- Statistics:", statistics.mean(valorMedioRGB))

print("\nModa imagem binária:", statistics.mode(rolBinaria))
print("Moda imagem tons de cinza:", statistics.mode(rolTonsDeCinza))
print("Moda imagem RGB:", statistics.mode(rolRGB))

print("\nMediana imagem binária:", statistics.median(rolBinaria))
print("Mediana imagem tons de cinza:", statistics.median(rolTonsDeCinza))
print("Mediana imagem RGB:", statistics.median(rolRGB))

cv2.waitKey(0)
cv2.destroyAllWindows()
