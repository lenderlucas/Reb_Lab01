#from unsupervised.SVD import SVD
from unsupervised.SDV import SVD
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Cargar la imagen en color
img = cv2.imread('./imagen/deep-learning.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Redimensionar la imagen a 256x256 píxeles
resized = cv2.resize(gray, (256, 256), interpolation=cv2.INTER_AREA)
imagen = resized

svd = SVD(n_vectors=250)
#Aplicar la clase .fit en la clase SDV.
image=svd.fit_transform(resized)
print(image.shape)
plt.imshow(image,cmap='gray')
plt.show()

#Aplicar la clase inverse_transform en la clase SDV.
reverse=svd.transform(resized)
print(reverse.shape)
plt.imshow(reverse,cmap='gray')
plt.show()

#Aplicar la clase inverse_transform en la clase SDV.
reverse=svd.inverse_transform()
print(reverse.shape)
plt.imshow(reverse,cmap='gray')
plt.show()

'''
img = svd.aplicar_valores(imagen)
cv2.imshow("Original", resized)
cv2.imshow("Reconstruida", img.astype(np.uint8))
cv2.waitKey(0)
'''

# Seleccionamos la imagen número 13 de la lista
image = image[12]
#Punto 4

#Primero se descompone la matriz de la imagen seleccionada
# Descomposición SVD
U, S, VT = np.linalg.svd(image, full_matrices=False)

#Luego, podemos reconstruir la imagen utilizando los valores singulares
#aumentando gradualmente el número de valores singulares utilizados:

    
# Número de valores singulares a utilizar
n = 10

# Reconstrucción de la imagen utilizando los n primeros valores singulares
image_approx = U[:,:n] @ np.diag(S[:n]) @ VT[:n,:]

#Para cuantificar las diferencias, podemos calcular la norma de 
#Frobenius entre la imagen original y la aproximación:
    
diff_norm = np.linalg.norm(image - image_approx, ord='fro')
print(f"Diferencia para {n} valores singulares: {diff_norm}")
  

#Podemos repetir este proceso para diferentes valores de n y graficar la norma 
#de Frobenius en función del número de valores singulares utilizados. 
#El punto en el que la norma de Frobenius alcanza un mínimo puede ser considerado 
#como el punto en el que la imagen se reproduce adecuadamente.

# Número máximo de valores singulares a utilizar
max_n = min(image.shape)

# Lista para almacenar las normas de Frobenius
diff_norms = []

# Recorremos los valores de n
for n in range(1, max_n):
    # Reconstrucción de la imagen utilizando los n primeros valores singulares
    image_approx = U[:,:n] @ np.diag(S[:n]) @ VT[:n,:]
    # Norma de Frobenius entre la imagen original y la aproximación
    diff_norm = np.linalg.norm(image - image_approx, ord='fro')
    diff_norms.append(diff_norm)

# Gráfico de la norma de Frobenius en función del número de valores singulares utilizados
plt.plot(range(1, max_n), diff_norms)
plt.xlabel('Número de valores singulares')
plt.ylabel('Norma de Frobenius')
plt.show()