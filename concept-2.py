
class Parent:

    def greet(self):
        return "Hello From Parent"

class Child(Parent):

    def __init__(self, title):
        self.title = title


    def greet(self):
        return super().greet()+" Hello From Child "+self.title

    # def helloGreet(self):
    #     print("Hello From Child")

c = Child("rohit deshpande qa engineer")
text = c.greet()
print(text)
# c.helloGreet()