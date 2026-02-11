##PHYTON LIST
#List dibuat dengan tanda kurung siku
thislist = ["apple", "banana", "cherry"]
print(thislist) 

#List dapat memiliki item dengan nilai yang sama
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Banyak item dalam list (Panjang List)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List bisa berisi tipe data apapun
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list1), type(list2), type(list3), type(list4))

#list() untuk membuat list baru
thislist = list(("apple", "banana", "cherry"))


##ACCES LIST ITEMS
#Akses item dengan nomor indeks
thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print(thislist[-1])

#Range indeks
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#in untuk menentukan ada/tidak item dalam list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


##CHANGES LIST ITEMS
#Ubah nilai item 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Mengubah nilai item dengan range tertentu
#1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert() untuk menyisipkan item tanpa mengganti nilai yg ada
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


##ADD LIST ITEMS
#append() untuk menambahkan item keakhir list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend() untuk menambahkan elemen dari list lain / tuple, set, dictionaries
#1
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#2
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
thisset = {"kiwi", "orange"}
thislist.extend(thisset)
print(thislist)


##REMOVE LIST ITEMS
#Hapus item yg ditentukan
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Hapus indeks yg ditentukan
#1
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#2
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#clear() untuk mengosongkan list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


##LOOP LIST
#Print semua item dalam list satu per satu
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#range() & len() untuk loop berdasarkan indeks
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#while & len() untuk loop berdasarkan indeks
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


##LIST COMPREHENSION
#List baru dengan sintaks yg lebih singkat
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#List baru dengan range()
newlist = [x for x in range(10) if x < 5]

#.upper() untuk ubah nilai dalam list baru jadi huruf kapital
newlist = [x.upper() for x in fruits]


##SORT LIST
#sort() mengurutkan list dari kecil ke besar
#1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#3
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#4
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#sort(reverse = True) mengurutkan list dari besar 
#1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#2
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#.reverse() membalikkan urutan list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


##COPY LIST
#.copy() 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list() 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#[:] 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


##JOIN LIST
#operator (+) menggabungkan 2 list ke variabel list baru
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#menambahkan item list lain ke list yang sudah ada
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

#extend() menambahkan item list lain ke list yang sudah ada
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)