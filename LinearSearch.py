#linear search
def linear_search(arr, target): #membuat fungsi bernama linear_search
    #cek setiap indeks dari awal sampai akhir
    for i in range(len(arr)): #len = jumlah
        #Kalau nilainya cocok dengan target
        if arr[i] == target:
            return i #hentikan pencarian, kembalikan indeksnya
    return -1 #kalau di cek semua gak ada, kembalikan -1. -1 nya itu artinya gak ada dalam indeks karena indeks selalu dimulai dari 0

data = [12, 7, 25, 9, 15]

target = 9

hasil = linear_search(data, target) #panggil fungsi dan simpan hasilnya

if hasil != -1:
    print("angka", target, "ada di indeks ke: ", hasil)
else:
    print("angka tidak ditemukan")