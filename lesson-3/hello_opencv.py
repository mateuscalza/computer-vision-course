import cv2

image = cv2.imread("./resources/lena.png")
cv2.imshow("Hello OpenCV!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
