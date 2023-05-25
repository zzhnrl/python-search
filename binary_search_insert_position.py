def cari_elemen(data, target):
    low = 0 
    high = len(data) -1
    insert_pos = 0 

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid

        if data[mid] < target:
            insert_pos = mid + 1
            low = mid + 1

        else:
            insert_pos = mid 
            high = mid - 1
    return insert_pos 

# Contoh input 
data = [2, 4, 6, 8, 10, 12, 14]
target = 9 

#Mencari posisi sisipan agar tetap terurut
posisi = cari_elemen(data, target)

#Menampilkan posisi sisipan
print("Elemen", target, "dapat disisipkan pada indeks", posisi, "untuk menjaga daftar tetap terurut.")