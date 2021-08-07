import cv2 as cv
import os
import numpy as np
from time import time

dataRuta = "M:/Python_Reconocimiento_facial/reconocimientofacial1/Data"
listaData = os.listdir(dataRuta)
# print('data',listaData)
ids = []
rostrosData = []
id = 0
tiempoInicial = time()
for fila in listaData:
    rutaCompleta = dataRuta + "/" + fila
    print("Iniciando lectura...")
    for archivo in os.listdir(rutaCompleta):

        print("Imagenes:", fila + "/" + archivo)
        print()
        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta + "/" + archivo, 0))
        # imagenes=cv.imread(rutaCompleta + "/" + archivo,0)

    id = id + 1
    tiempoFinalLectura = time()
    tiempoTotalLectura = tiempoFinalLectura - tiempoInicial
    print("Tiempo total lectura: ", tiempoTotalLectura)

entrenaminetoModeloEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
print("Iniciando el entrenamiento ... espere")
entrenaminetoModeloEigenFaceRecognizer.train(rostrosData, np.array(ids))
tiempoFinalEntrenamiento = time()
tiempoTotalEntrenamiento = tiempoFinalEntrenamiento - tiempoFinalLectura
print(
    "Tiempo entrenamiento total",tiempoTotalEntrenamiento
)
entrenaminetoModeloEigenFaceRecognizer.write("M:/Python_Reconocimiento_facial/reconocimientofacial1/Entranamiento_EigenFaceRecognizer.xml")
print("Entremianto concluido")
