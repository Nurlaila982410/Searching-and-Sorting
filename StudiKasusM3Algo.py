# #linear search
# #Cari nilai mahasiswa dalam list
# def linear_search(arr, target): #membuat fungsi bernama linear_search
#     #cek setiap indeks dari awal sampai akhir
#     for i in range(len(arr)): #len = jumlah
#         #Kalau nilainya cocok dengan target
#         if arr[i] == target:
#             return i #hentikan pencarian, kembalikan indeksnya
#     return -1 #kalau di cek semua gak ada, kembalikan -1. -1 nya itu artinya gak ada dalam indeks karena indeks selalu dimulai dari 0

# nilai_mahasiswa = [64, 80, 75, 93, 53]

# target = 75

# hasil = linear_search(nilai_mahasiswa, target) #panggil fungsi dan simpan hasilnya

# if hasil != -1:
#     print("Nilai", target, "ada di indeks ke: ", hasil)
# else:
#     print("Nilai tidak ditemukan")



# #BUBBLE SORT
# #Mengurutkan nilai mahasiswa
# def bubble_sort(arr):

#     n = len(arr)

#     for i in range(n):

#         for j in range(n-i-1):

#             if arr[j] > arr [j+1]:

#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr


# #data yang mau diurutkan
# nilai = [97, 56, 70, 84, 62]
# #panggil fungsi
# hasil = bubble_sort(nilai)
# #tamppilkan hasil
# print("Nilai sebelum di Urutkan: ", [97, 56, 70, 84, 62])
# print("Nilai setelah di Urutkan: ", hasil)



#linear search
#Cari kata dalam dokumen
def linear_search(arr, target): #membuat fungsi bernama linear_search
    #cek setiap indeks dari awal sampai akhir
    for i in range(len(arr)): #len = jumlah
        #Kalau nilainya cocok dengan target
        if arr[i] == target:
            return i #hentikan pencarian, kembalikan indeksnya
    return -1 #kalau di cek semua gak ada, kembalikan -1. -1 nya itu artinya gak ada dalam indeks karena indeks selalu dimulai dari 0

kata = ["aku", "dia", "Algoritma", "suka", "dan"]

target = "Algoritma"

hasil = linear_search(kata, target) #panggil fungsi dan simpan hasilnya

if hasil != -1:
    print("Kata", target, "ada di indeks ke: ", hasil)
else:
    print("Kata tidak ditemukan")