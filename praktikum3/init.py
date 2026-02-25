#CARA KERJA
class Person:
  def __init__(self, name, age):    #init dipanggil otomatis 
    self.name = name                #setiap kali kelas digunakan
    self.age = age                  #untuk buat objek baru

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


#KENAPA INIT
class Person:
  pass                              #Tanpa init

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):    #Dengan init
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)


#NILAI DEFAULT
class Person:
  def __init__(self, name, age=18): #Tetapkan nilai default pada age
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


#BEBERAPA PARAMETER
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
