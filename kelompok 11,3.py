# tugas uts bagian 3 
# Fungsi untuk bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Loop untuk membandingkan elemen
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar elemen jika tidak urut
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Fungsi untuk mencari nilai x dengan sequential search
def search_value(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Mengembalikan posisi index jika ditemukan
    return -1  # Mengembalikan -1 jika tidak ditemukan

# Himpunan A
A = [109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 
     31, 39, 900, 21, 378, 400, 101, 201, 301, 1]

# Soal 1: Mengurutkan himpunan A
print("Himpunan A sebelum diurutkan:")
print(A)

A_sorted = bubble_sort(A.copy())
print("\nHimpunan A setelah diurutkan (Bubble Sort):")
print(A_sorted)

# Soal 2: Mencari nilai x dalam himpunan A
x = 300  # Contoh nilai yang dicari
posisi = search_value(A_sorted, x)

if posisi != -1:
    print(f"\nNilai {x} ditemukan di posisi index ke-{posisi} (setelah diurutkan).")
else:
    print(f"\nNilai {x} tidak ditemukan dalam himpunan A.")