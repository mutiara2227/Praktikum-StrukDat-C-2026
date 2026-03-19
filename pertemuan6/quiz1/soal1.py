###PERBAIKAN###
def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("Harga harus diatas 1.000.000")
        return
    elif len(sn) < 5:
        print("SN harus berisi minimal 5 karakter")
        return
    
    return {
        "merk": merk,
        "tipe": tipe,
        "harga": harga,
        "sn": sn,
        "status": "Tersedia"
    }

def main():
    inventaris = []
    for x in range(3):
        merk = input("Masukkan merk: ")
        tipe = input("Masukkan tipe: ")
        harga = int(input("Masukkan harga: "))
        sn = input("Masukkan SN: ")
        print("==================\n")
        
        gadget = registrasi_gadget(merk, tipe, harga, sn)
        while gadget == None:
            merk = input("Masukkan merk: ")
            tipe = input("Masukkan tipe: ")
            harga = int(input("Masukkan harga: "))
            sn = input("Masukkan SN: ")
            print("==================\n")
            gadget = registrasi_gadget(merk, tipe, harga, sn)
        inventaris.append(gadget)
        
    print(inventaris)


if __name__ == "__main__":
    main()



###ASLI###
#Buat fungsi registrasi_gadget(merk, tipe, harga, sn) yang menerima 4 parameter. Merk(string), tipe(string), harga(float), sn(string)
def registrasi_gadget (merk, tipe, harga, sn):
    if harga <= 1000000 :
        print('Error : harga harus diatas 1.000.000')
        return None
    if len(sn) <5:
        print('Error : Serial Number harus berisi minimal 5 karakter')
        return None


    gadget = {
        'merk' : merk,
        'tipe' : tipe,
        'harga' : harga,
        'sn' : sn,
        'status' : 'Tersedia'
    } 
    return gadget

INVENTARIS = []
for x in range(3):
    print(f'Gadget {x+1}')

    merk = input('merk = ')
    tipe = input('tipe = ')
    harga = float(input('harga = '))
    sn = input ('Serial Number = ')
    gadget = registrasi_gadget (merk, tipe, harga, sn)
    if gadget:
        INVENTARIS.append(gadget)
    else:
        print('registrasi gagal')
    
    for item in INVENTARIS:
        print(item)