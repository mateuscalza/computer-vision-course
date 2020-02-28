import numpy as np
import cv2

image = cv2.cvtColor(cv2.imread('./resources/bruno.jpeg'), cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

dim = (image.shape[1], image.shape[0])
resized_image = cv2.resize(image, dsize=None, fx=0.65, fy=0.65, interpolation=cv2.INTER_AREA)

smoothed_image = cv2.GaussianBlur(resized_image, (7, 7), 0)

canny1 = cv2.Canny(smoothed_image, 10, 120)
canny2 = cv2.Canny(smoothed_image, 10, 170)

result = np.vstack([
  np.hstack([resized_image, smoothed_image]),
  np.hstack([canny1, canny2])
])
cv2.imshow("Canny", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
