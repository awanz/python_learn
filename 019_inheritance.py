class Person():
  def __init__(self, fname, lname):
    
    self.fname = fname
    self.lname = lname
    self.fullname = fname + " " + lname

  def printName(self):
    print("hello, ")
    print(self.fullname)

p1 = Person("Awan", "Star")
p1.printName()

class Employee(Person):
  pass

e1 = Employee("Juni", "Restina")
e1.printName()