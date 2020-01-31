import cv2
import numpy as np

desenho1 = np.zeros((400, 600), dtype="uint8")
desenho2 = np.zeros((400, 600), dtype="uint8")

desenho1[100:350, 25:400] = 255
desenho2[25:200, 300:550] = 255

cv2.imshow("Desenho1", desenho1)
cv2.imshow("Desenho2", desenho2)

res = cv2.bitwise_and(desenho1, desenho2)
cv2.imshow("AND", res)

res = cv2.bitwise_or(desenho1, desenho2)
cv2.imshow("OR", res)

res = cv2.bitwise_xor(desenho1, desenho2)
cv2.imshow("XOR", res)

res = cv2.bitwise_and(desenho1, cv2.bitwise_not(desenho2))
cv2.imshow("A AND [NOT(B)]", res)

res = cv2.bitwise_not(desenho1)
cv2.imshow("NOT", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
