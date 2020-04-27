import cv2

def nothing(x):
    pass

#cria janela de trackbars
cv2.namedWindow("trackbars")

cv2.createTrackbar("x","trackbars",0,800,nothing)
cv2.createTrackbar("y","trackbars",0,800,nothing)
cv2.createTrackbar("w","trackbars",100,800,nothing)
cv2.createTrackbar("h","trackbars",100,800,nothing)

#Captura video
cap = cv2.VideoCapture(0)

#criar loop para pegar todos os frames

while(True):
    #recupera trackbar
    x = cv2.getTrackbarPos("x","trackbars")
    y = cv2.getTrackbarPos("y","trackbars")
    w = cv2.getTrackbarPos("w","trackbars")
    h = cv2.getTrackbarPos("h","trackbars")
    #Recuperar Frame
    ret,frame = cap.read()
    roi = frame[y:h,x:w]

    cv2.imshow('Roi',roi)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#Libera o cache de cap
cap.release()
#Destroi todas as janelas abertas
cv2.destroyAllWindows()
            
