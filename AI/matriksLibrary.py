import numpy as np

# Mendefinisikan matriks A (2x3) dan B (3x4)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

# Menghitung perkalian matriks A * B
result = np.dot(A, B)

# Menampilkan hasil
print("Hasil perkalian matriks A * B:")
print(result)