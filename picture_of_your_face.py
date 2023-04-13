import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en color
img = cv2.imread('./imagen/deep-learning.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Redimensionar la imagen a 256x256 píxeles
resized = cv2.resize(gray, (256, 256), interpolation=cv2.INTER_AREA)

# Guardar la imagen editada
cv2.imwrite('./imagen/my_Imagen.jpg', resized)

# ruta donde se encuentran las imágenes
ruta_imagenes = './imagen/'

# leer todas las imágenes en la ruta
for filename in os.listdir(ruta_imagenes):
    # asegurarse de que el archivo es una imagen
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # leer la imagen y almacenarla en una matriz numpy
        imagen = cv2.imread(os.path.join(ruta_imagenes, filename))
        
        # realizar operaciones en la imagen (por ejemplo, mostrarla en una ventana)
        #cv2.imshow('Imagen', imagen)
        #cv2.waitKey(0)
        
# Ruta completa de las imágenes
path = ruta_imagenes

# Obtener los nombres de los archivos en la ruta
files = os.listdir(path)

# Filtrar los archivos para obtener solo las imágenes
image_files = [file for file in files if file.endswith('.jpg') or file.endswith('.png')]

# Agregar la ruta completa a cada nombre de archivo
full_paths = [os.path.join(path, file) for file in image_files]

# Imprimir la lista de nombres de archivo completos
#print(full_paths) 

# Cargar las imágenes de los rostros de tus compañeros de clase y convertirlas a escala de grises
classmates_filenames = full_paths
classmates_images = []
for filename in classmates_filenames:
    image = cv2.imread(filename)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    classmates_images.append(gray_image)

# Resize the images to the same size, if necessary
height, width = classmates_images[0].shape[:2]
resized_images = [cv2.resize(image, (width, height)) for image in classmates_images]

# Calculate the average face
mean_face = np.mean(resized_images, axis=0)

# Plot the average face
plt.imshow(mean_face, cmap='gray')
plt.show()

# Calculate the Euclidean distance between your face and the average face
your_image = cv2.imread('my_imagen.jpg')
your_gray_image = cv2.cvtColor(your_image, cv2.COLOR_BGR2GRAY)
resized_your_image = cv2.resize(your_gray_image, (width, height))
distance = np.linalg.norm(resized_your_image - mean_face)
print('Distance between your face and the average face: {:.2f}'.format(distance))