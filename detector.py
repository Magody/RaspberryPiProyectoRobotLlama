#clasificador de imagenes, caracteristicas HAAR, ambientes controlados
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('fire.xml') #se ocupa un modelo ya entrenado y se crea un archivo xml
cap = cv2.VideoCapture(0)
cap.set(3,300) #esto es max para un raspberry 
#cap.set(100,700)

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convierto a escala de grises, esto trabaja en 2 dimensiones

    faces = face_cascade.detectMultiScale(gray,1.3,5) #densidad y umbral
    if len(faces) != 0:
        print("Fuego")
    for (x,y,w,h) in faces: #devuelve posiciones de los rostros
        cv2.rectangle(frame,(x,y),(x + w , y + h), (255,0,0), 2)

    cv2.imshow('Fuego',frame) #muestra la pantalla
    s = cv2.waitKey(30) & 0xff
    if s == ord("s"):
        break
        
cap.release() #libero la camara  
cv2.destroyAllWindows()
