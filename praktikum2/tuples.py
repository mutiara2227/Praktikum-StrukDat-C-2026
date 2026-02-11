##PHYTON TUPLE
#Tuple ditulis dengan tanda kurung biasa
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple dapat memiliki item dengan nilai yang sama
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Banyak item dalam tuple (Panjang Tuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Jika tuple hanya 1 item, tetap beri koma 
thistuple = ("apple",)
print(type(thistuple))

#Tuple bisa berisi data apapun
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

#tuple() untuk membuat tuple baru
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


##ACCES TUPLE
#Akses item dengan nomor indeks
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])
print(thistuple[-1])

#Range indeks
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

#in untuk menentukan ada/tidak item dalam tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


##UPDATE TUPLE
#Ubah dulu ke List baru bisa di update
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#.append() untuk menambahkan item ke akhir tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#operator(+=) untuk menambahkan tuple kedalam tuple baru
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#.remove() untuk hapus item yg ditentukan
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#.clear() untuk mengosongkan tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.clear()
thistuple = tuple(y)
print(thistuple)


##UNPACK TUPLE
#Mengekstrak nilai kembali ke dalam variabel baru
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#operator(*) diawal nama variabel, jika jumlah variabel < jumlah nilai
#1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#2
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


##LOOP TUPLE
#Print semua item dalam tuple satu per satu
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#range() & len() untuk loop berdasarkan indeks
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#while & len() untuk loop berdasarkan indeks
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


##JOIN TUPLE
#operator (+) menggabungkan 2 tuple ke variabel tuple baru
tuple1 = ["a", "b", "c"]
tuple2 = [1, 2, 3]
tuple3 = tuple1 + tuple2
print(tuple3)

#operator (*) mengalikan isi tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)