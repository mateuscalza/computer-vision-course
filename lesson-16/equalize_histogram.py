import cv2
from matplotlib import pyplot as plt

imagemOriginal = cv2.imread("./resources/car.png", 0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow("Original image", imagemOriginal)
cv2.imshow("Equalized image", imagemEqualizada)

plt.hist(imagemOriginal.ravel(), 256, [0, 256])
plt.figure()

plt.hist(imagemEqualizada.ravel(), 256, [0, 256])
plt.show()
