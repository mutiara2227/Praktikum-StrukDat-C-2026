class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def tambahKendaraan(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

def hapusKendaraan(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

plat1 = Node('B 1234 ABC')
plat2 = Node('D 8888 XYZ')
plat3 = Node('A 111 TUV')
plat4 = Node('B 2022 EFG')

plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

newNode = Node('B 1222 MUT')
plat1 = tambahKendaraan(plat1, newNode, 2)
print('Setelah ditambahkan :')
traverseAndPrint(plat1)

plat1 = hapusKendaraan(plat1, plat4)
print('Setelah dihapus :')
traverseAndPrint(plat1)