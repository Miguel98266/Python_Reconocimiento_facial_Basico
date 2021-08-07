# Python_Reconocimiento_facial

## Instrucciones para tener una copia del proyecto;
1. Clona el repositorio del proyecto.
2. Ejecuta pip install opencv-python y pip install imutils en tu cmd .
3. Listo

## Desarrollado con:
-Python -Version 3.9

## Descripcion de archivos
* "Contorno.py" identificamos las conversiones a grises y a blanco y negro para poder detectar los bordes de la imagen a leer
 ![Contorno](/Imagenes/Contorno.PNG)
 
* "mostrarcamara.py" Este archivo sirve para poder conectar nuestra camara web con Python
* "contadormonedas.py" 
  ![monedas1](/Imagenes/monedas1.png)
  ![monedas2](/Imagenes/monedas2.png)
 * **Imagen original** es nuestro input de monedas el cual va analizar.
 * **Imagen en Grises** convierte nuestra imagen en escala de grises para que sea mas facil tu procesamiento.
 * **Imagen con Gauss** es un desenfoque gaussiano muy eficaz para eliminar el ruido gaussiano de una imagen.
 * **Imagen con Canny** Canny Edge Detection es un popular algoritmo de detección de bordes.
 * **Imagen Cierre** El cierre es inverso a la apertura, la dilatación seguida de la erosión . Es útil para cerrar pequeños agujeros dentro de los objetos en primer plano o  pequeños puntos negros en el objeto.
 * **Imagen Resultado con bordes** Es la imagen original con los bordes encontrados en la imagen. 

* "contadormonedascamara.py"
