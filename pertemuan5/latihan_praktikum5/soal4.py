#Diberikan data produk dalam bentuk list of dictionaries:
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]
#Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk Keyboard.
gudang_pc[1]['kategori'] = 'Aksesoris'
print(gudang_pc)
#Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
print(gudang_pc)
#Hitung Total Nilai Aset (Harga x Stok) untuk setiap item. Tampilkan output dengan
#format:
#Item: [Nama] | Total Aset: Rp [Hasil Perkalian]
for x in range(len(gudang_pc)):
    print(f'item:{gudang_pc[x]['item']} total aset:{gudang_pc[x]['harga']*gudang_pc[x]['stok']}')