import cv2

cam = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier('harr_face.xml')
cam.set(3,640)
cam.set(4,480)
cam.set(10,100)

while True :
     flag,img = cam.read()
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)

     print(f'number of the face detected = {len(faces)}')

     for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

     cv2.imshow("detected", img)
     if cv2.waitKey(1) and 0xFF == 27:break