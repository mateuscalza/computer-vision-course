import cv2

print(cv2.__version__)

fichasV = cv2.imread("./resources/1_ficha_vermelha_centro.png")
fichasP = cv2.imread("./resources/4_fichas_pretas.png")

fichas = cv2.add(fichasV, fichasP)

cv2.imshow("Hello OpenCV!", fichas)

cv2.waitKey(0)
cv2.destroyAllWindows()
