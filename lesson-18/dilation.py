import cv2

original_image = cv2.imread("./resources/rolamento.png", 0)

structuring = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (5, 5)
)

processed = cv2.dilate(
    original_image,
    structuring,
    iterations=10
)

cv2.imshow("Original", original_image)
cv2.imshow("Result", processed)

cv2.waitKey(0)
cv2.destroyAllWindows()
