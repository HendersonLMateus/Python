import cv2
import numpy as np

def nothing(x):
    pass

#cria janela de trackbars
cv2.namedWindow("track")

cv2.createTrackbar("th","track",0,255,nothing)
cv2.createTrackbar("ero","track",0,10,nothing)
cv2.createTrackbar("dil","track",0,10,nothing)
cv2.createTrackbar("opn","track",0,10,nothing)
cv2.createTrackbar("clo","track",0,10,nothing)

#Captura video
cap = cv2.VideoCapture(0)

#criar loop para pegar todos os frames

while(True):
    #recupera trackbar
    th = cv2.getTrackbarPos("th","track")
    ero = cv2.getTrackbarPos("ero","track")
    dil = cv2.getTrackbarPos("dil","track")
    opn = cv2.getTrackbarPos("opn","track")
    clo = cv2.getTrackbarPos("clo","track")
    #Recuperar Frame
    ret,frame = cap.read()
    
    #criar frame cinza
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    #Criar threshold
    ret,thres = cv2.threshold(gray,th,255,cv2.THRESH_BINARY)

    #Criar Kernel
    kernel = np.ones((5,5),np.uint8)

    #Eosao
    erosion = cv2.erode(thres,kernel,iterations = ero)

    #Dilatação
    dilate = cv2.dilate(thres,kernel,iterations = dil)

    #Opening
    opening = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel, iterations = opn)

    #Closing
    closing = cv2.morphologyEx(thres,cv2.MORPH_CLOSE, kernel, iterations = clo)

    #exibir
    #cv2.imshow('Blur',blur)
    #cv2.imshow('Gray',gray)
    #cv2.imshow('Erosao',erosion)
    #cv2.imshow('Dilate',dilate)
    cv2.imshow('Closing',clo)
    cv2.imshow('Opening',opening)
    cv2.imshow('Thresh',thres)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#Libera o cache de cap
cap.release()
#Destroi todas as janelas abertas
cv2.destroyAllWindows()
            
