class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
    
    def traverse_preorder(self, node, result):
        if node is not None:
            result.append(node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)

    def traverse_inorder(self, node, result):
        if node is not None:
            self.traverse_inorder(node.left, result)
            result.append(node.data)
            self.traverse_inorder(node.right, result)

    def traverse_postorder(self, node, result):
        if node is not None:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)

    def get_leaf_nodes(self, node, leaf_list):
        if node:
            if node.left is None and node.right is None:
                leaf_list.append(node.data)
            self.get_leaf_nodes(node.left, leaf_list)
            self.get_leaf_nodes(node.right, leaf_list)
        return leaf_list

print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.\n")

a = BinaryTree()
a.insert_root('A')
a.insert_left(a.root, 'B')
a.insert_right(a.root, 'C')
a.insert_left(a.root.left, 'D')
a.insert_right(a.root.left, 'E')
a.insert_right(a.root.right, 'F')

pre = []
ino = []
post = []
leaf = []

a.traverse_preorder(a.root, pre)
a.traverse_inorder(a.root, ino)
a.traverse_postorder(a.root, post)
a.get_leaf_nodes(a.root, leaf)

print("HASIL AUDIT:")
print("1. Pre-Order :", " - ".join(pre))
print("2. In-Order :", " - ".join(ino))
print("3. Post-Order :", " - ".join(post))
print()
print("[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf))
print("======================================")
print("Audit Selesai!")
