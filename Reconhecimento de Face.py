import cv2
import os
import numpy as np

#Funções
def savePerson():
    global ultimoNome
    global boolsaveImg
    print("Qual seu nome?")
    name = input()
    ultimoNome = name
    boolsaveImg = True

def saveImg(img):
    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists(f'train/{ultimoNome}'):
        os.makedirs(f'train/{ultimoNome}')
     
    files = os.listdir(f'train/{ultimoNome}')
    cv2.imwrite(f'train/{ultimoNome}/{str(len(files))}.jpg', img)

def trainData():
    global recognizer
    global trained
    global persons
    trained = True
    persons = os.listdir('train')
    ids = []
    faces = []

    for i,p in enumerate(persons):
        for f in os.listdir(f'train/{p}'):
            img = cv2.imread(f'train/{p}/{f}', 0)
            faces.append(img)
            ids.append(i)

    recognizer.train(faces,np.array(ids))        


trained = False 
ultimoNome = ""
boolsaveImg = False
savecount = 0
persons = []
recognizer = cv2.face.LBPHFaceRecognizer_create() 

cap = cv2.VideoCapture(0)

#carregar o haar cascade

face_cascade = cv2.CascadeClassifier("C:\\Users\PANDA CRAZ1\Desktop\Mateus\Python\OpenCv\haarcascade-frontalface-default.xml")

while(True):
    
    ret,frame = cap.read()
    

    #criar gray
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    #Detectar faces na imagem
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    #Correr todas as faces encontradas
    for (x,y,w,h) in faces:
        #roi da face
        roi = gray[y:y+h,x:x+w]
        roi = cv2.resize(roi,(50,50))
        #Desenhar o retangulo em volta da face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        if trained:
            idf, conf = recognizer.predict(roi)
            nameP = persons[idf]
            print(nameP)
            cv2.putText(frame,nameP,(x,y), 3,0.5,(0,255,0),1, cv2.LINE_AA)

        if boolsaveImg == True:
            saveImg(roi)
            savecount += 1

        if savecount > 150:
            boolsaveImg = False
            savecount = 0

    #cv2.imshow('gray',gray)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1)

    #Slavar Imagens
    if key == ord('s'):
        savePerson()
    
    if key == ord('t'):
        trainData()

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
