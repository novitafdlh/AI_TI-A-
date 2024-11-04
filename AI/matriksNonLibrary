# Mendefinisikan matriks A (2x3) dan B (3x4)
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]

# Matriks hasil perkalian A * B
# Ukuran hasil = (baris A) x (kolom B)
result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

# Loop untuk menghitung perkalian matriks
for i in range(len(A)):               # Iterasi baris dari A
    for j in range(len(B[0])):        # Iterasi kolom dari B
        for k in range(len(B)):       # Iterasi elemen dalam baris A dan kolom B
            result[i][j] += A[i][k] * B[k][j]

# Menampilkan hasil
print("Hasil perkalian matriks A * B:")
for row in result:
    print(row)