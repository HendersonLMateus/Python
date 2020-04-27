import cv2
import numpy as np
#Captura videos
cap = cv2.VideoCapture("carros.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)

#criar loop para pegar todos os frames

while(True):
    #Recuperar Frame
    ret,frame = cap.read()
    
    mask = subtractor.apply(frame)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 1)
    mask = cv2.dilate(mask,kernel,iterations = 1)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel, iterations = 1)
    mask = cv2.dilate(mask,kernel,iterations = 1)


    #Coloca contorno nas coisas
    contours,h =cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >1500:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)

    
    key = cv2.waitKey(30)

    if key == ord('q'):
        break

#Libera o cache de cap
cap.release()
#Destroi todas as janelas abertas
cv2.destroyAllWindows()
            
