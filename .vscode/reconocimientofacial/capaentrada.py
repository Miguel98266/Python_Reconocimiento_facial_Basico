import cv2 as cv
import os 

modelo='FotosMiguel'
ruta1='M:/Python_Reconocimiento_facial/reconocimientofacial1'
rutacompleta=ruta1+ '/' + modelo
if not os.path.exists(rutacompleta):
    os.makedirs(rutacompleta)


ruidos=cv.CascadeClassifier('M:\Python_Reconocimiento_facial\entrenamientos opencv ruidos\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
camara=cv.VideoCapture(0)
id=0
while True:
    respuesta,captura=camara.read()
    if respuesta==False:
        break
    grises=cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    idcaptura=captura.copy()
    cara=ruidos.detectMultiScale(grises,1.3,5)
    for(x,y,e1,e2) in cara:
        cv.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
    cv.imshow('Resultado rostro',captura)

    if cv.waitKey(1)==ord('s'):
        break
camara.release()
cv.destroyAllWindows()