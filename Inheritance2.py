class Animal():
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some generic animal sounds"

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"
    
dog = Dog("Naruto")
cat = Cat("Sasuke")

print(dog.name)
print(dog.make_sound())    
print(cat.name)
print(cat.make_sound())
