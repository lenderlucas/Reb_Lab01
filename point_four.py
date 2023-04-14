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