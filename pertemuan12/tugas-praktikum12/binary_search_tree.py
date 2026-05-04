class TreeNode:
  def __init__(self, id_buku, judul):
    self.id_buku = id_buku
    self.judul = judul
    self.left = None
    self.right = None

def insert(node, id_buku, judul):
    if node is None:
        print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
        return TreeNode(id_buku, judul)
    
    if id_buku < node.id_buku:
        node.left = insert(node.left, id_buku, judul)
    else:
        node.right = insert(node.right, id_buku, judul)
    return node

def search(node, id_buku):
    if node is None:
        return None
    if id_buku == node.id_buku:
        return node
    elif id_buku < node.id_buku:
        return search(node.left, id_buku)
    else:
        return search(node.right, id_buku)

def traversal_inorder(node):
    if node is None:
        return
    traversal_inorder(node.left)
    print(f'{node.id_buku} - {node.judul}')
    traversal_inorder(node.right)

def get_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
    
def get_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def height(node):
    if node is None:
        return -1
    return max(height(node.left), height(node.right))+1


print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print('=========================================')

node = None

node = insert(node, 50, 'Dasar Pemrograman')
node = insert(node, 30, 'Struktur Data')
node = insert(node, 70, 'Kecerdasan Buatan')
node = insert(node, 20, 'Matematika Diskrit')
node = insert(node, 40, 'Basis Data')
node = insert(node, 60, 'Jaringan Komputer')
node = insert(node, 80, 'Sistem Operasi')

print('\n[INFO] Koleksi Buku (In-Order Traversal) : ')
traversal_inorder(node)

print('\n[SEARCH] Mencari ID 60...', end=" ")
hasil = search(node, 60)
if hasil:
    print(f'Ditemukan! Judul: {hasil.judul}')
else:
    print('Data tidak ditemukan.')

print('[SEARCH] Mencari ID 100...', end=" ")
hasil = search(node, 100)
if hasil:
    print(f'Ditemukan! Judul: {hasil.judul}')
else:
    print('Data tidak ditemukan.')

print(f'\n[STATISTIK] ID Terkecil: {get_min(node).id_buku}')
print(f'[STATISTIK] ID Terbesar: {get_max(node).id_buku}')

print(f'[INFO] Tinggi (Height) Tree: {height(node)}')

print("=========================================")
