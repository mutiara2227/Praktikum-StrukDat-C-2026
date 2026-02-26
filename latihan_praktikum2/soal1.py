#Diberikan sebuah list yang merepresentasikan jumlah stok barang di gudang:
stok = [15, 50, 30, 25, 40]
#Tambahkan stok baru sebesar 100 ke akhir list.
stok.append(100)
print(stok)
#Sisipkan angka 75 di posisi indeks ke-2.
stok.insert(2, 75)
print(stok)
#Urutkan list tersebut dari yang terbesar ke terkecil.
stok.sort(reverse = True)
print(stok)
#Hitunglah nilai rata-rata dari seluruh stok tersebut. cara manual
rata = (100+75+50+40+30+25+15)/7
print('Rata-rata =',rata)
#Hitunglah nilai rata-rata dari seluruh stok tersebut. cara cepat
rata_rata = sum(stok)/len(stok)
print('Rata-rata =',rata_rata)
#Tampilkan isi list setelah semua perubahan dilakukan.
print(stok,'Rata-rata =',rata)