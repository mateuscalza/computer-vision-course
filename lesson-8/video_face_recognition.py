import cv2

cascade_har = cv2.CascadeClassifier(
    "./resources/haarcascade_frontalface_default.xml")

if cascade_har.empty():
    raise Exception("Error! XML not found.")

capture = cv2.VideoCapture("./resources/people.mp4")

while capture.isOpened():
    result, frame = capture.read()
    if result != True:
        raise Exception("Error! Frame was not captured")
    faces = cascade_har.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=5)

    print("Faces: ", len(faces))
    for(coord_x, coord_y, width, height) in faces:
        cv2.rectangle(frame, (coord_x, coord_y), (coord_x +
                                                width, coord_y + height), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Pessoa", (coord_x, coord_y),
                    font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("Image", frame)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
