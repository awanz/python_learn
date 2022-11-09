class MyNumber():
  numb = 15

testNumb = MyNumber()
print(testNumb.numb)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"{self.name} ({self.age})"

  def welcome(self):
    print("Welcome, " + self.name)

people = Person("Awan", 27)
print(people.name)
print(people.age)
print(people)
people.welcome()