from cv2 import cv2
imagen=cv2.imread('M:/Python_Reconocimiento_facial/contadormonedas/contorno.jpg')
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
tipoUmbral,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(65,105,225),3)
#1 Contorno
#-1 Todos los contornos
#Mostrar
cv2.imshow('Imagen Original',imagen)
cv2.imshow('Imagen en Grises',grises)
cv2.imshow('Imagen Umbral',umbral)
print(tipoUmbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
