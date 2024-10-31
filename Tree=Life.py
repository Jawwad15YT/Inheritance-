class Tree:
    def __init__(self, height, age):
        self.height = height
        self.age = age

    def grow(self):
        print("The tree is growing.")

class Mango(Tree):
    pass

class Banana(Tree):
    pass

mango_tree = Mango("15 feet", "10 years")
banana_tree = Banana("8 feet", "2 years")

mango_tree.grow()
banana_tree.grow()

print(mango_tree.height)