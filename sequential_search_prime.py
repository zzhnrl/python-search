def prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cari_bil_prima(n):
    Prima = []
    for num in no:
        if prima(num):
            Prima.append(num)
    return Prima

#Daftar bilangan
no = [7, 10, 13, 6, 17, 22, 19]

#Mencari bilangan prima dalam daftar bilangan
prima_no = cari_bil_prima(no)

#Menampilkan bilangan prima yang terdapat dalam daftar bilangan
print("Bilangan prima yang terdapat dalam daftar : ", prima_no)