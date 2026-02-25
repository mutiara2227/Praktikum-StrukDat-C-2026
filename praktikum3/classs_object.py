#MEMBUAT CLASS
class MyClass:  #Gunakan kata kunci class
  x = 5         #Properti

print(MyClass)


#MEMBUAT OBJECT
class MyClass:
  x = 5

p1 = MyClass()  #Objek
print(p1.x)     #Cetak nilai x


#BEBERAPA OBJEK
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


#pass STATEMENT
class Person:
  pass


#HAPUS OBJECT
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1      #Gunakan kata kunci del

print(p1)   #Akan error karena objek sudah dihapus




