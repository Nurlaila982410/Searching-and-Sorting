# #linear search
# def linear_search(arr, target): #membuat fungsi bernama linear_search
#     #cek setiap indeks dari awal sampai akhir
#     for i in range(len(arr)): #len = jumlah
#         #Kalau nilainya cocok dengan target
#         if arr[i] == target:
#             return i #hentikan pencarian, kembalikan indeksnya
#     return -1 #kalau di cek semua gak ada, kembalikan -1. -1 nya itu artinya gak ada dalam indeks karena indeks selalu dimulai dari 0

# data = [4, 7, 1, 9]

# target = 7

# hasil = linear_search(data, target) #panggil fungsi dan simpan hasilnya

# if hasil != -1:
#     print("angka", target, "ada di indeks ke: ", hasil)
# else:
#     print("angka tidak ditemukan")



# #binary search
# def binary_search(arr, target):
#     left = 0                     #batas kiri
#     right = len(arr) -1          #batas kanan
    
# #selama batas kiri dan kanan belum bersilang
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid #ketemu! kembalikan indeksnya
#         elif target < arr[mid]:
#             right = mid -1 #target lebih kecil, geser ke batas kanannya
#         else:
#             left = mid + 1 #target lebih besar, geser ke batas kanan
#     return -1 #kalau di cek sampai habis gak ada, kembali

# data = [2, 4, 6, 8, 10]

# angka_dicari = 8

# hasil = binary_search(data, angka_dicari)

# if hasil != -1:
#     print("angka", angka_dicari, "ada di indeks", hasil)
# else:
#     print("angka tidak ditemukan")


#BUBBLE SORT
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            if arr[j] > arr [j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


#data yang mau diurutkan
data = [9, 3, 5, 1]
#panggil fungsi
hasil = bubble_sort(data)
#tamppilkan hasil
print("Data sebelum di Sorting: ", [9, 3, 5, 1])
print("data setelah di sorting: ", hasil)




# #Ke bawah seterusnya itu opsional
# #SELECTION SORT
# def selection_sort(arr):

#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# data = [9, 3, 5, 1]
# hasil = selection_sort(data)
# print("Hasil Sorting: ", hasil)


# #INSERTION SORT
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
        
#     return arr

# data = [9, 3, 5, 1]
# hasil = insertion_sort(data)
# print("Hasil Sorting: ", hasil)



# #MERGE SORT
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         while i < len(left) and j < len (right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i+= 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1

#     return arr

# data = [9, 3, 5, 1]
# hasil = merge_sort(data)
# print("Hasil Sorting: ", hasil)


# #QUICK SORT
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left =[]
#     middle = []
#     right = []
#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         elif x > pivot:
#             right.append(x)
#         else:
#             middle.append(x)
#     return quick_sort(left) + middle + quick_sort(right)

# data = [9, 3, 5, 1]
# hasil = quick_sort(data)
# print("Hasil Sorting: ", hasil)