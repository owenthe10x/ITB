#NIM        :   19622270
# Nama       :   Owen Tobias Sinurat
# Deskripsi  :   Problem 3

# KAMUS
#x, y, i, length, divider, cantique = int

x = int(input("Masukkan X: "))
y = x
i = 1

# ini perulangan utama yang saya gunakan untuk mengalikan x dengan i yang incremental
while(1 == 1):
    divider = 0
    # perulangan ini saya gunakan untuk mengetahui jumlah digit dari y
    for j in range(10):
        if((y*i)//(10**j) < 1):
            length = j
            break
    # perulangan ini saya gunakan untuk mencari divider dengan digit yang sama yaitu 1 dan jumlah digit sama dengan y
    for k in range(length):
        divider = divider+(10**k)
    # ini merupakan case untuk break dari loop, yaitu saat y habis dibagi oleh divider
    if((y*i) % divider == 0):
        cantique = y*i
        break
    # ini adalah proses increment dari i agar perkaliannya dapat berjalan ke depan
    i += 1

print("Bilangan cantik terkecil yang habis dibagi ", x, " ialah ", cantique)
