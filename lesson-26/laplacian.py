import cv2

image = cv2.imread('./resources/bruno.jpeg')
cv2.imshow("Original", image)

image_result = cv2.Laplacian(image, cv2.CV_8U)
cv2.imshow("Result", image_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
