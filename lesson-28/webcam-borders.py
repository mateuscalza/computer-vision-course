import cv2

cap = cv2.VideoCapture(0)

scale = 1
delta = 0

while True:
  _, frame = cap.read()
  frame = cv2.resize(frame, dsize=None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
  image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
  sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)

  abs_sobel_x = cv2.convertScaleAbs(sobel_x)
  abs_sobel_y = cv2.convertScaleAbs(sobel_y)

  grad_xy = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
  
  image_smooth = cv2.GaussianBlur(image_gray, (3, 3), 1)
  edges = cv2.Canny(image_smooth, 30, 110)

  laplacian = cv2.Laplacian(image_smooth, cv2.CV_64F, ksize=3)
  laplacian_result = laplacian / laplacian.max()

  cv2.imshow("Laplacial", laplacian_result)
  cv2.imshow("X Sobel", abs_sobel_x)
  cv2.imshow("Y Sobel", abs_sobel_y)
  cv2.imshow("XY Sobel", grad_xy)
  cv2.imshow("Canny", edges)

  key = cv2.waitKey(10)
  if key == 27:
    break

cv2.destroyAllWindows()
cap.release()
