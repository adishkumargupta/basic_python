#doc string
"""
Animal class is a parent class
"""

class Animal:
    """ __init__ class is a constructor class for Animal class"""
    def __init__(self):
        print("Parent Animal Class")

""" Dog class inharit Animal class"""
class Dog(Animal):
    """ __init__ class is a constructor class for Dog class"""
    def __init__(self, name, age):
        """We add the variable in global variable"""
        self.name = name
        self.age = age
    def brow():
        print("Hello brow")

cls = Dog("adish",34)
print(cls.name)
print(cls.age)
cls.brow()

print(Dog.__doc__)