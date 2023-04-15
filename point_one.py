import numpy as np

# We generate a random rectangular matrix of size 3x4
A = np.random.rand(3, 4)

#The rank of a rectangular matrix is ​​the maximum number of columns or rows that are linearly independent.
rango = np.linalg.matrix_rank(A)

# The trace of a matrix is ​​the sum of the elements of its main diagonal.
traza = np.trace(A)

#The determinant of a rectangular matrix is ​​undefined, since it is only defined for square matrices.
submatrix = A[:3, :3]

# Calcular el determinante de la submatriz
det_submatrix = np.linalg.det(submatrix)
print("El determinante de la submatriz es:", det_submatrix)

#To invert a rectangular matrix A, we need it to have full rank, that is, all its columns or 
# rows are linearly independent. In this case, we can use singular value decomposition (SVD) to get the inverse

A_inv = np.linalg.pinv(A)

# Calculamos la SVD de A
U, S, Vt = np.linalg.svd(A)

# Calculamos A'A y AA'
ATA = np.dot(A.T, A)
AAT = np.dot(A, A.T)

# Calculamos los valores propios y vectores propios de A'A
eigvals_ATA = S**2
eigvecs_ATA = Vt.T

# Calculamos los valores propios y vectores propios de AA'
eigvals_AAT = S**2
eigvecs_AAT = U

# Imprimimos los resultados
print("Valores propios y vectores propios de A'A:")
print("Valores propios:")
print(eigvals_ATA)
print("Vectores propios:")
print(eigvecs_ATA)
print("Valores propios y vectores propios de AA':")
print("Valores propios:")
print(eigvals_AAT)
print("Vectores propios:")
print(eigvecs_AAT)