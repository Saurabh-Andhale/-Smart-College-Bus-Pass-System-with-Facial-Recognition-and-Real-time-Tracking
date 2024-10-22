import cv2
from PIL import Image

face_cascade=cv2.CascadeClassifier('/home/ashutosh/Desktop/elon/face_detector.xml')
# 1.creating a video object
while True:
    face_id=input('Enter your id : ')
    face_name=input('Enter your Name : ')
    cap = cv2.VideoCapture(0) 
    # 2. Variable
    a = 0
    # 3. While loop
    while True:
        a = a + 1
        # 4.Create a frame object
        check, img = cap.read()
        # Converting to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.1,4)
        # 5.show the frame!
        for(x,y,w,h)in faces:
            x,y=x-40,y-40
            w,h=w+80,h+80
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("Capturing",img)
        # 6.for playing 
        key = cv2.waitKey(1)
        if key == ord(' '):
            im = img[y:y + h, x:x + w]
            # im1 = im.resize(300,300)
            im1=cv2.resize(im,(300,300))
            showPic = cv2.imwrite("/home/ashutosh/Desktop/elon/ImagesAttendance/" + str(face_id) + ',' + str(face_name) + ".jpg",im1)
            print(showPic)
            
            cap.release()
            cv2.destroyAllWindows 
            break
    
    cap.release()
    cv2.destroyAllWindows 
