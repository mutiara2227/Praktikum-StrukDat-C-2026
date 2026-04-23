#================================================
#1. Parkir Dua Arah — Penelusuran Maju & Mundur
#================================================
class Node:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Menambah kendaraan ke akhir list
    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return

        # Cari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Hubungkan node terakhir dengan node baru
        current.next = new_node
        new_node.prev = current
    
    # Mencetak semua kendaraan  dari head ke tail
    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.plat, end='\n')
            current = current.next

    
    # Mencetak semua kendaraan dari tail ke head
    def tampilkan_mundur(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next

        # Tampilkan mundur
        while current:
            print(current.plat, end='\n')
            current = current.prev



a = DoublyLinkedList()

a.tambah_kendaraan('B 1234 ABC')
a.tambah_kendaraan('D 5678 XYZ')
a.tambah_kendaraan('A 9999 TUV')

print('[Maju]')
a.tampilkan_maju()

print('\n[Mundur]')
a.tampilkan_mundur()


#================================================
#2. Hapus Kendaraan dari Tengah — Update Dua Arah
#================================================
class Node:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Menambah kendaraan ke akhir list
    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return

        # Cari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Hubungkan node terakhir dengan node baru
        current.next = new_node
        new_node.prev = current
    
    # Mencetak semua kendaraan  dari head ke tail
    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.plat, end='\n')
            current = current.next
    
    # Menghapus node berdasarkan plat
    def hapus_kendaraan(self, plat):
        current = self.head

        while current:
            if current.plat == plat:
                # Jika node pertama
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                    current.prev.next = current.next

                    if current.next:
                      # Menghubungkan node berikutnya dengan node sebelumnya
                        current.next.prev = current.prev
                return

            current = current.next


b = DoublyLinkedList()

b.tambah_kendaraan('B 1111 AA')
b.tambah_kendaraan('D 2222 BB')
b.tambah_kendaraan('A 3333 CC')
b.tambah_kendaraan('B 4444 DD')

print('\nSebeleum:')
b.tampilkan_maju()

b.hapus_kendaraan('A 3333 CC')

print('\nSesudah:')
b.tampilkan_maju()

print('\n')

#====================================================
#3. Antrean Giliran Petugas Valet — Rotasi Melingkar
#====================================================
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def tambah_petugas(self, nama):
        new_node = Node(nama)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Sambungkan node terakhir ke node baru
        current.next = new_node
        new_node.next = self.head

    #Mensimulasikan n kali giliran dan mencetak nama petugas yang bertugas setiap gilirannya
    def giliran_berikutnya(self, n):
        if self.head is None:
            print('Tidak ada petugas.')
            return

        current = self.head

        for i in range(1, n + 1):
            print(f'Giliran {i}: {current.nama}')
            current = current.next


c = CircularLinkedList()

c.tambah_petugas('Andi')
c.tambah_petugas('Budi')
c.tambah_petugas('Citra')
c.tambah_petugas('Dewi')
c.giliran_berikutnya(6)