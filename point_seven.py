from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
mnist = fetch_openml('mnist_784')

X = mnist.data[(mnist.target == '0') | (mnist.target == '8')]
y = mnist.target[(mnist.target == '0') | (mnist.target == '8')]
y = y.astype(int)

# Reducción de dimensionalidad con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualización con scatter plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='jet')
plt.colorbar()
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()