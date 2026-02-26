#Diberikan list stok barang di gudang: stok_barang = [15, 40, 30, 10, 25]
stok_barang = [15, 40, 30, 10, 25]
#Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
stok_barang[3] = 50
print(stok_barang)
#Tambahkan nilai 5 ke akhir list, kemudian urutkan list secara descending (besar ke kecil).
stok_barang.append(5)
print(stok_barang)
stok_barang.sort(reverse = True)
print(stok_barang)
#Tampilkan jumlah total seluruh nilai dalam list tersebut.
jumlah = sum(stok_barang)
print(jumlah)
#Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai dalam list > 20, jika tidak tampilkan "Waspada".
rata = jumlah/len(stok_barang)
print('Rata-rata =',rata)
status = 'Stok Aman' if rata > 20 else 'Waspada'
print(status)