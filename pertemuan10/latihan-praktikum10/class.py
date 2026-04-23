class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "None"
        return self.items[-1]

    def size(self):
        return len(self.items)

a = StackList()

a.push('https://www.w3schools.com/python/python_dsa_stacks.asp')
a.push('https://www.youtube.com/')
a.push('https://ft.unri.ac.id/')

print("Riwayat: ", a.items)
print("Hapus URL: ", a.pop())
print("Riwayat setelah dihapus: ", a.items)
print("URL Teratas: ", a.peek())
print("Riwayat kosong(True)/tidak(False): ", a.is_empty())
print("Total URL: ", a.size())