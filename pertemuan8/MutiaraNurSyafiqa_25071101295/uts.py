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




