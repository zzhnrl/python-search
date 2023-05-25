def binary_search(dictionary, target):
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        if dictionary[mid][0] == target:
            return dictionary[mid][1]
        elif dictionary[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Definisi kata tidak ditemukan"

#Isi List / element
dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

target_word = input("Masukkan kata yang ingin dicari definisinya : ")
definition = binary_search(dictionary, target_word)

#Menampilkan definisi dari element
print(f"Definisi kata '{target_word}': {definition}")
