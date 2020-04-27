import cv2
import numpy as np

def nothing(x):
    pass

digits = cv2.imread('digits.png',0)

rows = np.vsplit(digits,50)
cells = []
for row in rows:
    row_cell = np.hsplit(row,50)
    for cell in row_cell:
      cell = cell.flatten()
      cells.append(cell)  

cells = np.array(cells, dtype=np.float32)
k = np.arange(10)
cells_labels = np.repeat(k,250)

knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)

#cria janela de trackbars
cv2.namedWindow("trackbars")

cv2.createTrackbar("x","trackbars",50,800,nothing)
cv2.createTrackbar("y","trackbars",90,800,nothing)
cv2.createTrackbar("w","trackbars",450,800,nothing)
cv2.createTrackbar("h","trackbars",350,800,nothing)
cv2.createTrackbar("th","trackbars",127,255,nothing)

#Captura video
cap = cv2.VideoCapture(0)

#criar loop para pegar todos os frames

while(True):
    #recupera trackbar
    x = cv2.getTrackbarPos("x","trackbars")
    y = cv2.getTrackbarPos("y","trackbars")
    w = cv2.getTrackbarPos("w","trackbars")
    h = cv2.getTrackbarPos("h","trackbars")
    th = cv2.getTrackbarPos("th","trackbars")
    #Recuperar Frame
    ret,frame = cap.read()
    roi = frame[y:h,x:w]

    #Gray roi
    gray = cv2.cvtColor(roi,cv2.COLOR_RGB2GRAY)

    #Criando Threshold

    ret, threshold = cv2.threshold(gray,th,255,cv2.THRESH_BINARY_INV)
    
    kernel = np.ones((5,5),np.uint8)

    dilate = cv2.dilate(threshold,kernel,iterations = 1)

    contours,h =cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 50:
            x2,y2,w2,h2 = cv2.boundingRect(cnt)

            cv2.rectangle(roi,(x2 , y2), (x2+w2 , y2+h2),(0,255,0),2)


    cv2.imshow('dilate',dilate)
    cv2.imshow('threshold',threshold)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#Libera o cache de cap
cap.release()
#Destroi todas as janelas abertas
cv2.destroyAllWindows()
            
