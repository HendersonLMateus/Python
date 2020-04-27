import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#carregar o haar cascade

face_cascade = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")

while(True):
    
    ret,frame = cap.read()
    

    #criar gray
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    #Detectar faces na imagem
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    #Correr todas as faces encontradas
    for (x,y,w,h) in faces:
        #roi da face
        roi = frame[y:y+h,x:x+w]
        roi = cv2.resize(roi,(10,10))
        roi = cv2.resize(roi,(w,h))

        frame[y:y+h,x:x+w] = roi
        #Desenhar o retangulo em volta da face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        
    
    #cv2.imshow('gray',gray)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
