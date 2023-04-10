import numpy as np

# We generate a random rectangular matrix of size 3x4
A = np.random.rand(3, 4)

#The rank of a rectangular matrix is ​​the maximum number of columns or rows that are linearly independent.
rango = np.linalg.matrix_rank(A)


# The trace of a matrix is ​​the sum of the elements of its main diagonal.
traza = np.trace(A)

#The determinant of a rectangular matrix is ​​undefined, since it is only defined for square matrices.
pass

#To invert a rectangular matrix A, we need it to have full rank, that is, all its columns or 
# rows are linearly independent. In this case, we can use singular value decomposition (SVD) to get the inverse

A_inv = np.linalg.pinv(A)

# How are eigenvalues and eigenvectors of A’A and AA’ related? What interesting differences can you notice between both?

'''The eigenvalues ​​and eigenvectors of A'A and AA' are related by 
the fact that they are similar matrices, that is, they have the same 
eigenvalues ​​but the eigenvectors can be different. In particular, if A is 
a rectangular matrix of size m x n, then A'A and AA' are square matrices 
of size n x n and m x m, respectively. Also, if matrix A has full rank, then A'A and AA' 
are positive definite and symmetric matrices, so all their eigenvalues ​​are nonnegative'''

'''
An interesting difference between A'A and AA' is that A'A 
can have eigenvalues ​​equal to zero, while AA' cannot have 
eigenvalues ​​equal to zero if A has full rank. This is because 
the rank of A'A is determined by the number of linearly independent columns of A, 
while the rank of AA' is determined by the number of linearly independent rows of A.
If A has fewer rows than columns, then AA' cannot have full rank and therefore 
cannot have eigenvalues ​​equal to zero.
'''