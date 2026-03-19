def ganjil_genap (plat):
    ganjil = []
    genap = []
    for x in plat:
        huruf = x.split()
        angka = huruf[1]
        angka_terakhir = int(angka[-1])

        if angka_terakhir % 2 == 0:
            genap.append(x)
        else:
            ganjil.append(x)
    return ganjil, genap

plat_nomor = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = ganjil_genap (plat_nomor)

print('Plat Ganjil : ',ganjil)
print('Plat Genap : ', genap)
