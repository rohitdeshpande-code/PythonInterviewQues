

class Person:

    def __init__(self, name, age): #Constructor
        self.name = name #Instance variable
        self.age = age

    def greet(self): #Instance method
        return f"Hello, my name is {self.name}, my age is {self.age}"

#Creating an object
person1 = Person("John", 33)

#calling the instance method
message = person1.greet()
print(message) #Hello, my name is John, my age is 33

