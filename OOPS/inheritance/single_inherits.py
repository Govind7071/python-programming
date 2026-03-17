class Animal :
    def __init__(self, name):
        self.name = name


class Type (Animal):
    def __init__ (self,name,brand) :
        super().__init__(name)
        self.brand = brand



my_animal=Type("dog","german")

print(f"{my_animal.name} : { my_animal.brand}")