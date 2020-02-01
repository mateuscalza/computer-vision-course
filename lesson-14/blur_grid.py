import cv2
import numpy as np

img = cv2.imread('./resources/lena.jpg')
img = img[::2, ::2]

suave = np.vstack([
    np.hstack([img,                   cv2.blur(img, (3, 3))]),
    np.hstack([cv2.blur(img, (5, 5)), cv2.blur(img, (7, 7))]),
    np.hstack([cv2.blur(img, (9, 9)), cv2.blur(img, (11, 11))]),
])

cv2.imshow("Smoothed image - blur", suave)

cv2.waitKey(0)
cv2.destroyAllWindows()
