class Animal:
    def walk(self):
        print('Walking')

class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
       print("Dog barks ghew ghew")
mydog=Dog("Doggy",7)
print(mydog.name)
print(mydog.age)
mydog.bark()
mydog.walk()
