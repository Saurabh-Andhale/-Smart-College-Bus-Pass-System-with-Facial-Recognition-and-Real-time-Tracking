import cv2
from grpc import Status
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv
# from PIL import ImageGrab
 
face_cascade=cv2.CascadeClassifier('/home/ashutosh/Desktop/elon/face_detector.xml')

path = '/home/ashutosh/Desktop/elon/ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

now = datetime.now()
dtString = now.strftime('%H:%M:%S')


with open('/home/ashutosh/Desktop/elon/Attendance/Attendance.csv','w',newline='')as fp:
        a=csv.writer(fp,delimiter=',')
        data=[['Roll no','Names','Time']]
        a.writerows(data)
 
def markAttendance(name):
    names=name.find(',')
    name1=name[0:names]
    name2=name[names+1:]
    
    
    with open('/home/ashutosh/Desktop/elon/Attendance/Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name1 not in nameList:
            
            f.writelines(f'\n{name1},{name2}')
 
#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
 
encodeListKnown = findEncodings(images)
print('Encoding Complete')
 
cap = cv2.VideoCapture(0)
 
while True:
    success, img = cap.read()
    #img = captureScreen()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
 
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),1)
            cv2.line(img,(x1,y1),(x1+30,y1),(255,0,255),3)
            cv2.line(img,(x1,y1),(x1,y1+30),(255,0,255),3)
            cv2.line(img,(x2,y2),(x2-30,y2),(255,0,255),3)
            cv2.line(img,(x2,y2),(x2,y2-30),(255,0,255),3)
            cv2.line(img,(x2,y1),(x2-30,y1),(255,0,255),3)
            cv2.line(img,(x2,y1),(x2,y1+30),(255,0,255),3)
            cv2.line(img,(x1,y2),(x1+30,y2),(255,0,255),3)
            cv2.line(img,(x1,y2),(x1,y2-30),(255,0,255),3)
            # cv2.rectangle(img,(x1,y2-35),(x2,y2),(255,0,255),cv2.FILLED)
            cv2.putText(img,name,(x1+15,y2+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
            #cv2.putText(img,f'{int(faces.score[0]*100)}%')
            markAttendance(name)
        # else:
        #     for(x,y,w,h)in faces:
        #         x,y=x-40,y-40
        #         w,h=w+80,h+80
        #         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            
            
            # print(name1
 
    cv2.imshow('Webcam',img)
    key=cv2.waitKey(1)
    if key == 27:
        break

cap.release()
# print(name)
cv2.destroyAllWindows()
