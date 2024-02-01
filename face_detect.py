import cv2 # using pip install opencv-python in system terminal

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
# xml file which is prewritten and makes it easier to use facial detection

image = cv2.imread("test.jpg", 1)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

face = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (225, 0, 0), 2)

cv2.imshow("img" , image)
cv2.waitKey()
cv2.imwrite("face_detected.jpg")