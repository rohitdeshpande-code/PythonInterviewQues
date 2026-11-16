

class MyClass:

    @classmethod
    def class_method(cls):
        return "Inside class method"

    def instance_method(self):
        return "Inside instance method"


# obj = MyClass()
print(MyClass.class_method())
# print(obj.instance_method())