# Matriks A
A = [
    [11, 55, 54, 10],
    [23, 5, 23, 17],
    [21, 17, 13, 11],
    [11, 17, 14, 15]
]

# Matriks B
B = [
    [3, 0, 0, 1],
    [8, 1, 0, 8],
    [3, 0, 1, 3],
    [1, 0, 0, 3]
]

# Inisialisasi matriks hasil
result = [[0 for _ in range(4)] for _ in range(4)]

# Perkalian matriks secara manual
for i in range(4):  # Baris matriks A
    for j in range(4):  # Kolom matriks B
        for k in range(4):  # Elemen untuk dikalikan
            result[i][j] += A[i][k] * B[k][j]

# Output hasil
print("Hasil perkalian matriks A x B:")
for row in result:
    print(row)
