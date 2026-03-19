#Diberikan sebuah tuple barang:
barang = ("B001", "Laptop Gaming", 15000000)
#Akses dan tampilkan harga barang dari tuple tersebut.
print(barang[2])
#Cobalah untuk mengubah harga barang menjadi 14000000. Jelaskan dalam komentar kode mengapa hal ini menyebabkan error (Gunakan comment).
y = list(barang)
y[2] = 14000000
barang = tuple(y)
print(barang)
#Gunakan teknik unpacking untuk memasukkan isi tuple ke dalam tiga variabel: kode, nama, dan harga.
(kode, nama, harga) = barang
print(kode)
print(nama)
print(harga)