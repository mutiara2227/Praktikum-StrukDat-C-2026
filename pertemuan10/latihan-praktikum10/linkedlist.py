class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 #Variabel bantuan untuk melacak ukuran
    
    def is_empty(self):
        return self.count == 0
    
    def push(self,url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self):
        if self.is_empty():
            return 'Riwayat Kosong'
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    
    def peek(self):
        if self.is_empty():
            return 'None'
        return self.top.url
    
    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end="->")

            currentNode = currentNode.next
        print()

a = StackLinkedList()

a.push('https://www.w3schools.com/python/python_dsa_stacks.asp')
a.push('https://www.youtube.com/')
a.push('https://ft.unri.ac.id/')

print('Riwayat: ', end="")
a.traverseAndPrint()
print("URL Teratas: ", a.peek())
print("Hapus URL: ", a.pop())
print("Riwayat setelah dihapus: ", end="")
a.traverseAndPrint()
print("Riwayat kosong(True)/tidak(False): ", a.is_empty())
print("Total URL: ", a.size())
