import cv2

image = cv2.imread('./resources/bruno.jpeg', 0)
cv2.imshow("Original", image)

# X
sobelX = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=3)
cv2.imshow("Sobel X", sobelX)

# Y
sobelY = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=3)
cv2.imshow("Sobel Y", sobelY)

# XY
sobelXY1 = cv2.Sobel(image, cv2.CV_8U, 1, 1, ksize=3)
cv2.imshow("Sobel XY", sobelXY1)

# X or Y
sobelXY2 = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X - bitwise - Sobel Y", sobelXY2)

cv2.waitKey(0)
cv2.destroyAllWindows()
