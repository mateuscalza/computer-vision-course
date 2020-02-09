import cv2 

imgOriginal = cv2.imread("./resources/4_fichas_pretas.png", 0) 

metodo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imgOriginal, 50, 255, metodo) 

cv2.imshow("Imagem Original", imgOriginal) 
cv2.imshow("Imagem Tratada", imgBinarizada) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
