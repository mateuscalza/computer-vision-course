import cv2

imagem = cv2.imread("./resources/lena.png")
cv2.imshow("Ola Lena", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
