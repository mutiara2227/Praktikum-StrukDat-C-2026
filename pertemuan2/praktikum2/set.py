##PHYTON SET
#Set ditulis dengan kurung kurawal
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Dua item dengan nilai yg sama akan diabaikan
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True dan 1 dianggap nilai yg sama
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#False dan 0 dianggap nilai yg sama
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#Banyak item dalam set (Panjang Set)
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set bisa berisi tipe data apapun
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

#set() untuk membuat set baru
thisset = set(("apple", "banana", "cherry")) 


##ACCES SET ITEM
#1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#3
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


##ADD SET ITEMS
#.add() untuk menambahkan 1 item 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#.update() untuk menambahkan item dari set lain /tuple, list, dictionary ke set saat ini
#1
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#2
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


##REMOVE SET ITEMS
#.remove() atau .discard() untuk menghapus item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)

#.pop() hapus item secara acak
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

#.clear() mengosongkan set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

##LOOP SET
#Print semua item dalam set satu per satu
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


##JOIN SET
#.union() atau operator(|) untuk gabungkan set jadi set baru
#1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)
#2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
myset = set1 | set2 | set3 |set4
print(myset)

#.union() gabung set dengan tipe data lain
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#.update() memasukkan semua item dari satu set ke set lain
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#.intersection atau operator (&) mengembalikan set baru yang berisi item yang ada di kedua set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)

#True dan 1 dianggap nilai yg sama, begitu juga False dan 0
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#.difference() atau operator (-) menyimpan semua item set saat ini yang tidak ada di set lain
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
set3 = set1 - set2
print(set3)

#.symetric_difference() menyimpan item yang tidak ada di kedua-dua nya
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2
print(set3)


##FROZENSET
#frozenset() membuat set dari tipe data apapun yang tidak dapat diubah dari 
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
