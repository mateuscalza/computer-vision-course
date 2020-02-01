import cv2

image = cv2.imread('./resources/lena.jpg')

mask = (11, 11)
kernel = 11

blur = cv2.blur(image, mask)

sigma = 5
gaussian_blur = cv2.GaussianBlur(image, mask, sigma)

median_blur = cv2.medianBlur(image, kernel)

b_kernel = 11
s_color = 75
s_space = 75
bilateral_blur = cv2.bilateralFilter(image, b_kernel, s_color, s_space)

cv2.imshow('Imagem original', image)
cv2.imshow('Filtro de media (blur)', blur)
cv2.imshow('Filtro gaussiano', gaussian_blur)
cv2.imshow('Filtro de mediana', median_blur)
cv2.imshow('Filtro bilateral', bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
