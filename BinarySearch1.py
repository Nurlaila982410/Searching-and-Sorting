#binary search
def binary_search(arr, target):
    left = 0                     #batas kiri
    right = len(arr) -1          #batas kanan
    
#selama batas kiri dan kanan belum bersilang
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid #ketemu! kembalikan indeksnya
        elif target < arr[mid]:
            right = mid -1 #target lebih kecil, geser ke batas kanannya
        else:
            left = mid + 1 #target lebih besar, geser ke batas kanan
    return -1 #kalau di cek sampai habis gak ada, kembali

data = [10, 20, 30, 40, 50]

angka_dicari = 40

hasil = binary_search(data, angka_dicari)

if hasil != -1:
    print("angka", angka_dicari, "ada di indeks", hasil)
else:
    print("angka tidak ditemukan")
