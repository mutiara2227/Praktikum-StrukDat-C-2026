#ATURAN PENGGUNAAN
class NamaClass:
    def __init__(self, parameter):
        self.parameter = parameter


#AKSES ATRIBUT
class Person:
  def __init__(self, name, age):
    self.name = name        #self untuk akses
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()


#PANGGIL METHOD
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()      #self utk panggil method lain
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()
