import cv2

# Cargar la imagen en color
img = cv2.imread('mi_imagen.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Redimensionar la imagen a 256x256 píxeles
resized = cv2.resize(gray, (256, 256), interpolation=cv2.INTER_AREA)

# Guardar la imagen editada
cv2.imwrite('mi_imagen_editada.jpg', resized)


#Para trazar mi cara editada, se podría utilizar el siguiente código en Python:
import cv2
import numpy as np

# Cargar la imagen editada
img = cv2.imread('mi_imagen_editada.jpg')

# Crear una cascada de clasificación para detectar caras
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detectar la cara en la imagen
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

# Dibujar un rectángulo alrededor de la cara
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Mostrar la imagen con la cara detectada
cv2.imshow('Mi cara', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
Para calcular y trazar la cara media de la cohorte, se podría utilizar 
la técnica de Eigenfaces, que consiste en calcular los componentes principales de 
las caras de la cohorte y utilizarlos para reconstruir una cara media. 
El siguiente código en Python podría servir como ejemplo:
'''
import cv2
import numpy as np

# Cargar las imágenes de la cohorte
img1 = cv2.imread('imagen1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('imagen2.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('imagen3.jpg', cv2.IMREAD_GRAYSCALE)
# ...
imgN = cv2.imread('imagenN.jpg', cv2.IMREAD_GRAYSCALE)

# Convertir las imágenes a vectores de características
X = np.array([img1.flatten(), img2.flatten(), img3.flatten(), ..., imgN.flatten()])

# Calcular la media de las imágenes
mean_face = np.mean(X, axis=0)

# Calcular los componentes principales de las caras
cov = np.cov(X.T)
eigenvalues, eigenvectors = np.linalg.eig(cov)
idx = eigenvalues.argsort()[::-1]
eigenvectors = eigenvectors[:, idx]
eigenvalues = eigenvalues[idx]

# Elegir los primeros k componentes principales para reconstruir la cara media
k = 10
weights = eigenvectors[:, :k].T.dot(X - mean_face)
mean_reconstructed = mean_face + eigenvectors[:, :k].dot(weights)

# Redimensionar la cara media a 256x256 pí
