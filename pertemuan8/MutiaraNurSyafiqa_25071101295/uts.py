#####PERBAIKAN#####
#Soal 1 - List dan Dictionary
pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False},
]


# Menampilkan seluruh data pengunjung
def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama    | Usia | Kategori | Status")
    print("---+------+---------+------+----------+--------------")

    # Loop semua data pengunjung
    for i, p in enumerate(pengunjung_hari_ini, 1):
        # Menentukan status pengembalian
        status = "Belum Kembali" if not p["kembali"] else "Sudah Kembali"
        print(f"{i}  | {p['id']} | {p['nama']:<7} | {p['usia']}   | {p['kategori']:<8} | {status}")


# Filter pengunjung yang belum mengembalikan buku
def filter_belum_kembali():
    # List comprehension untuk mengambil data belum kembali
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]

    # Mengurutkan nama secara alfabet
    belum.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI =====")

    # Menampilkan hasil
    for i, nama in enumerate(belum, 1):
        print(f"{i}. {nama}")

    # Menampilkan total
    print("Total belum kembali:", len(belum), "pengunjung")



#Soal 2 - Tuple dan Set
# Informasi tetap perpustakaan menggunakan tuple
def info_perpustakaan():
    info = ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru", "0761-54321")

    print("Info Perpustakaan:")
    print("Nama  :", info[0])
    print("Alamat:", info[1])
    print("Telp  :", info[2])


# Rekap kategori menggunakan set dan dictionary
def rekap_kategori():
    # Set untuk menyimpan kategori unik
    kategori_set = set(p["kategori"] for p in pengunjung_hari_ini)

    # Dictionary untuk menghitung jumlah tiap kategori
    rekap = {}

    for p in pengunjung_hari_ini:
        kat = p["kategori"]
        rekap[kat] = rekap.get(kat, 0) + 1

    print("\nKategori Buku Unik:", kategori_set)
    print("Jumlah kategori:", len(kategori_set))

    print("\nRekap per kategori:")

    # Cari nilai maksimum
    max_jumlah = max(rekap.values())
    kategori_terbanyak = []

    # Tampilkan hasil rekap
    for k, v in rekap.items():
        print(f"{k} : {v} pengunjung")
        if v == max_jumlah:
            kategori_terbanyak.append(k)

    print("\nKategori terbanyak:", ", ".join(kategori_terbanyak), f"({max_jumlah} pengunjung)")



#Soal 3 - OOP
# Class dasar Pengunjung
class Pengunjung:
    # Variabel class untuk menghitung total objek
    counter = 0

    def __init__(self, id, nama, kategori):
        # Atribut private
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori

        # Tambah counter setiap objek dibuat
        Pengunjung.counter += 1

    # Getter ID
    def get_id(self):
        return self.__id

    # Getter Nama
    def get_nama(self):
        return self.__nama

    # Getter Kategori
    def get_kategori(self):
        return self.__kategori

    # Menampilkan data pengunjung
    def tampilkan_info(self):
        print(f"ID : {self.__id}")
        print(f"Nama : {self.__nama}")
        print(f"Kategori : {self.__kategori}")

    # Static method untuk total pengunjung
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.counter


# Class turunan untuk pengunjung prioritas
class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    # Override method tampilkan_info
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas : {self.prioritas}")

        # Jika mendesak, tampilkan peringatan
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")



#Soal 4 - Single Linked List: Antrian Peminjaman
# Node untuk menyimpan data antrian
class Node:
    def __init__(self, data):
        self.data = data   # data berupa dictionary
        self.next = None   # pointer ke node berikutnya


# Class Antrian menggunakan Single Linked List
class AntrianPeminjaman:
    def __init__(self):
        self.head = None  # awal antrian

    # Menambah pengunjung di akhir antrian
    def tambah(self, data):
        node = Node(data)

        # Jika antrian kosong
        if self.head is None:
            self.head = node
        else:
            temp = self.head

            # cari posisi terakhir
            while temp.next:
                temp = temp.next

            temp.next = node

    # Menampilkan seluruh antrian
    def tampilkan(self):
        print("\n===== ANTRIAN PEMINJAMAN =====")
        temp = self.head
        i = 1

        while temp:
            d = temp.data
            print(f"[{i}] {d['id']} - {d['nama']} | {d['kategori']}")
            temp = temp.next
            i += 1

        print("Total antrian:", self.hitung())

    # Memanggil pengunjung paling depan (FIFO)
    def panggil_berikutnya(self):
        if self.head:
            print("\nMemanggil pengunjung berikutnya...")
            print(f"Silakan masuk: {self.head.data['nama']} ({self.head.data['id']}) - {self.head.data['kategori']}")
            self.head = self.head.next

    # Mencari pengunjung berdasarkan nama
    def cari(self, nama):
        temp = self.head
        pos = 1

        while temp:
            if temp.data["nama"] == nama:
                print(f"\nDitemukan: {temp.data['id']} - {temp.data['nama']} | posisi ke-{pos}")
                return
            temp = temp.next
            pos += 1

        print("\nTidak ditemukan")

    # Menghapus berdasarkan ID (3 kasus)
    def hapus_berdasarkan_id(self, id):
        temp = self.head
        prev = None

        while temp:
            if temp.data["id"] == id:

                # jika node pertama
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print(f"\n{temp.data['nama']} ({id}) berhasil dihapus dari antrian.")
                return

            prev = temp
            temp = temp.next

        print("\nID tidak ditemukan")

    # Menghitung jumlah antrian
    def hitung(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count







#####ASLI#####
"""STUDI KASUS: SISTEM ANTRIAN PEMINJAMAN PERPUSTAKAAN
Sebuah perpustakaan kampus ingin membangun sistem digital
untuk mengelola proses peminjaman buku. Sistem ini harus mampu
menyimpan data pengunjung, mengelompokkan kategori buku yang dipinjam,
mencatat status pengembalian, dan mengatur antrian layanan petugas."""

#DATA AWAL YANG TERSEDIA#
data_pengunjung = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False}
]

#Soal 1 - List dan Dictionary
def tampilkan_pengunjung():
    print("=" * 55)
    print(f"{'ID':<6} {'Nama':<10} {'Usia':<10} {'Kategori':<15} {'Kembali':<15}")
    print("=" * 55)

    for pengunjung in data_pengunjung:
        print(f"{pengunjung['id']:<6} {pengunjung['nama']:<10} {pengunjung['usia']:<10} {pengunjung['kategori']:<15} {pengunjung['kembali']:<15}")

    print("=" * 55)

def filter_belum_kembali():
    print('=====PENGUNJUNG BELUM KEMBALI=====')
    for x in data_pengunjung:
        if x['kembali'] == False:
            print(x['nama'])

print('=====DATA PENGUNJUNG PERPUSTAKAAN=====')
tampilkan_pengunjung()
filter_belum_kembali()
filtered = [x for x in data_pengunjung if x['kembali'] == False]
filtered.sort (key=lambda x: x["nama"])
print('Total belum kembali: ',len(filtered))






#Soal 2 - Tuple dan Set
#Buat fungsi info_perpustakaan() — Kembalikan informasi tetap perpustakaan menggunakan tuple lalu tampilkan isinya.
def info_perpustakaan():
    informasi =(
        'Nama : Perpustakaan Kampus Terpadu',
        'Alamat : Jl. Pendidikan No. 5', 
        'Pekanbaru Telp : 0761-54321'
    )
    #Menampilkan isi tuple
    print('\nInfo Perpustakaan:')
    print(informasi[0])
    print(informasi[1])
    print(informasi[2])

#Buat fungsi rekap_kategori() — Gunakan set untuk mendapatkan kategori buku unik, lalu hitung jumlah pengunjung per kategori menggunakan dictionary.
def rekap_kategori():
    #Kategori buku dalam list
    jenis = ['Fiksi','Sains','Hukum','Fiksi','Sains','Hukum']

    #Mengambil jenis buku unik dengan set
    unik = set(jenis)
    #Tampilkan jenis buku unik
    print('\nKategori Buku Unik : ',unik)
    print('Jumlah Kategori : ',len(unik))

    #Menghitung jumlah pengunjung perkategori menggunakan dict
    rekap = {}
    for x in jenis:
        if x in rekap:
            rekap[x] += 1
        else:
            rekap[x] = 1
    
    #Menampilkan rekap
    print('\nRekap per kategori')
    for x, jumlah in rekap.items():
        print(f'{x} : {jumlah} pengunjung')
    
    #Menentukan jumlah kategori terbanyak
    max_jumlah = max(rekap.values())
    kategori_terbanyak = []
    for y,z in rekap.items():
        if z == max_jumlah:
            kategori_terbanyak.append(y)
    
    #Menampilkan kategori dengan jumlah pengunjung terbanyak
    print('\nKategori terbanyak : ',' , ' .join(kategori_terbanyak),f'({max_jumlah} pengunjung)')

#Panggil Ffingsi
info_perpustakaan()
rekap_kategori()






#Soal 3 - OOP
#Buat class induk pengunjung
class Pengunjung:
    #untuk nampung jumlah pengunjung
    jumlah_pengunjung = 0
    
    def __init__ (self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
    
        #Menghitung jumlah pengunjung
        Pengunjung.jumlah_pengunjung += 1
    
    #getter untuk setiap atribut
    def get_id(self):
        return self.__id
    def get_nama(self):
        return self.__nama
    def get_kategori(self):
        return self.__kategori
    
    #Method tampilkan info
    def tampilkan_info():
        print('ID       : ',self.__id)
        print('Nama     : ',self.__nama)
        print('Kategori : ',self.__kategori)
    
    #Method static hitung_pengunjung() -> mengembalikan total objek Pengunjung yang
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.jumlah_pengunjung
    
#Class pengunjung prioritas turunan class pengunjung
class PengunjungPrioritas(Pengunjung):
    def __init__ (self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        #Atribut tambahan
        self.prioritas = prioritas
    
    def tampilkan_info():
        print('ID           : ',self.get_id)
        print('Nama         : ',self.get_nama)
        print('Kategori     : ',self.get_kategori)
        print('Prioritas    : ',self.prioritas)

        #Jika prioritas = "Mendesak", tampilkan pesan peringatan: "** Layani segera! **"
        if self.prioritas == 'Mendesak':
            print('** Layani Segera! **')

#Buat objek dari kelas pengunjung
p1 = Pengunjung('M001','Rina','Fiksi')
#Buat objek dari kelas turunan
p2 = PengunjungPrioritas('M007','Gilang','Referensi','Mendesak')

p1.tampilkan_info()
print()
p2.tampilkan_info()
print()

#Tampilkan jumlah pengunjung
print('Total Pengunjung Terdaftar: ', Pengunjung.hitung_pengunjung())







#Soal 4 - Single Linked List: Antrian Peminjaman
print('===== ANTRIAN PEMINJAMAN =====')
print('[1] M001 - Rina      | Fiksi')
print('[2] M002 - Hendra    | Sains')
print('[3] M003 - Siti      | Fiksi')
print('[4] M004 - Taufik    | Hukum')
print('Total Antrian: 4')
print('\nMemanggil pengunjung berikutnya...')
print('Silakan masuk: Rina (M001) - Fiksi')
print('\n===== ANTRIAN PEMINJAMAN =====')
print('[1] M002 - Hendra    | Sains')
print('[2] M003 - Siti      | Fiksi')
print('[3] M004 - Taufik    | Hukum')
print('Total antrian: 3')
print('Menghapus pengunjung dengan ID M003...')
print('Siti (M003) berhasil dihapus dari antrian.')
print('\n===== ANTRIAN PEMINJAMAN =====')
print('[1] M002 - Hendra | Sains')
print('[2] M004 - Taufik | Hukum')
print('Total antrian: 2')
print('\nMencari "Taufik"...')
print('Ditemukan: M004 - Taufik | Hukum (posisi ke-2)')
print('\nTotal antrian: 2')




