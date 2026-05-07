class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[], [], [], [], [], [], [], [], [], []]

    def hash(self, kode):
        jumlah = 0
        for huruf in kode:
            jumlah += ord(huruf)
        index = jumlah % self.size
        return index
    
    def insert(self, kode, judul):
        index = self.hash(kode)
    
        for data in self.table[index]:
            if data[0] == kode:
                data[1] = judul
                print("Data diupdate")
                return

        self.table[index].append([kode, judul])
        print("Data ditambahkan")

    def search(self, kode):
        index = self.hash(kode)
        for data in self.table[index]:
            if data[0] == kode:
                print(kode, ":", data[1])
                return
        print("Buku tidak ditemukan")
    
    def delete(self, kode):
        index = self.hash(kode)
        for data in self.table[index]:
            if data[0] == kode:
                self.table[index].remove(data)
                print("Data berhasil dihapus")
                return
        print("Buku tidak ditemukan")

    def display(self):
        print("\nISI HASH TABLE")

        for i in range(self.size):
            print("Bucket", i, ":", self.table[i])

buku = HashTable()

buku.insert("BK111", "Mahir C++ Dalam Satu Jam")
buku.insert("BK222", "Python Dasar")
buku.insert("BK333", "Matematika Diskrit")
buku.insert("BK444", "Atomic Habits")

buku.display()

print("\nTambah Data Baru")

buku.insert("BK045", "Mein Kampf")
buku.insert("BK111", "Bumi Manusia")

buku.display()

print("\nCari Buku")

buku.search("BK222")
buku.search("BK999")

print("\nHapus Buku")

buku.delete("BK333")

buku.display()