class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


dog = Dog("Naruto")
cat = Cat("Sasuke")

print(dog.name)         
print(dog.make_sound()) 
print(cat.name)         
print(cat.make_sound()) 