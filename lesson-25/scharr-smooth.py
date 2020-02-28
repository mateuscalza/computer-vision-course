import cv2

image = cv2.imread('./resources/bruno.jpeg')
cv2.imshow("Source", image)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image_gray)

# Soft
image_soft = cv2.GaussianBlur(image_gray, (11, 11), 1)
cv2.imshow("Smooth", image_soft)

# X
sobel_x = cv2.Scharr(image_soft, cv2.CV_64F, 1, 0)
cv2.imshow("Scharr X", sobel_x)

# Y
sobel_y = cv2.Scharr(image_soft, cv2.CV_64F, 0, 1)
cv2.imshow("Scharr Y", sobel_y)

# XY
abs_sobel_x = cv2.convertScaleAbs(sobel_x)
abs_sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_xy = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
cv2.imshow("Enhanced Scharr XY", sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
