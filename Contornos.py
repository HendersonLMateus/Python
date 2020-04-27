import cv2
import numpy as np

def nothing(x):
    pass

#cria janela de trackbars
cv2.namedWindow("track")

cv2.createTrackbar("l-h","track",0,255,nothing)
cv2.createTrackbar("l-s","track",0,255,nothing)
cv2.createTrackbar("l-v","track",0,255,nothing)
cv2.createTrackbar("u-h","track",255,255,nothing)
cv2.createTrackbar("u-s","track",255,255,nothing)
cv2.createTrackbar("u-v","track",255,255,nothing)

#Captura video
cap = cv2.VideoCapture(0)

#criar loop para pegar todos os frames

while(True):
    #recupera trackbar
    lh = cv2.getTrackbarPos("l-h","track")
    ls = cv2.getTrackbarPos("l-s","track")
    lv = cv2.getTrackbarPos("l-v","track")
    uh = cv2.getTrackbarPos("u-h","track")
    us = cv2.getTrackbarPos("u-s","track")
    uv = cv2.getTrackbarPos("u-v","track")

    #Criar lower e upper
    lower = np.array([lh,ls,lv])
    upper = np.array([uh,us,uv])
    
    #Recuperar Frame
    ret,frame = cap.read()

    #Converter RGB para HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)

    #Criar Mascara
    mask = cv2.inRange(hsv,lower,upper)

    #Detectar contornos
    contours,h =cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Desenhar contornos
    cv2.drawContours(frame,contours,-1,(255,0,0),3)
    
    #exibir
    cv2.imshow('mask',mask)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#Libera o cache de cap
cap.release()
#Destroi todas as janelas abertas
cv2.destroyAllWindows()
            
