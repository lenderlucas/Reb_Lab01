#Cargamos la base de datos
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargamos los datos de MNIST
mnist = fetch_openml('mnist_784')

# Filtramos los ejemplos que corresponden a los dígitos 0 y 8
X = mnist.data[(mnist.target == '0') | (mnist.target == '8')]
y = mnist.target[(mnist.target == '0') | (mnist.target == '8')]

# Convertimos las etiquetas a valores binarios
y = (y == '8').astype(int)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

# Creamos un modelo de regresión logística
model = LogisticRegression(penalty='none',max_iter=1000)

# Entrenamos el modelo en los datos de entrenamiento
model.fit(X_train, y_train)

# Predecimos las etiquetas de los datos de prueba
y_pred = model.predict(X_test)

# Calculamos la exactitud del modelo
accuracy = accuracy_score(y_test, y_pred)

print("Exactitud de la línea de base: {:.2f}%".format(accuracy*100))