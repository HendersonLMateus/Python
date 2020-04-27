import cv2
import numpy as np

def nothing(x):
    pass

#Captura video
cap = cv2.VideoCapture("video.mp4")

#Subtractor
subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)

#criar loop para pegar todos os frames

while(True):
    #Recuperar Frame
    _,frame = cap.read()

    #Criar Mascara
    mask = subtractor.apply(frame)

    kernel = np.ones((5,5),np.uint8)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 1 )
    closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE, kernel, iterations = 1)
    dilate = cv2.dilate(closing,kernel,iterations = 4)

    
    #Detectar contornos
    contours,h =cv2.findContours(dilate,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Desenhar contornos
    cv2.drawContours(frame,contours,-1,(255,0,0),3)
    #exibir
    cv2.imshow('dilate',dilate)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#Libera o cache de cap
cap.release()
#Destroi todas as janelas abertas
cv2.destroyAllWindows()
            
