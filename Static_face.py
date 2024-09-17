import cv2

img = cv2.imread("resources/group_of_people2.jpg")
img = cv2.resize(img,(720,720))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


haar_cascade = cv2.CascadeClassifier('harr_face.xml')
faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=3)

print(f'number of the face detected = {len(faces)}')

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("detected",img)
if cv2.waitKey(0) and 0xFF==27:cv2.destroyAllWindows()