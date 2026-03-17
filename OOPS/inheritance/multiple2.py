class Parent1 :
    def __init__(self,name):
        self.name = name

    def info(self) : 
        print(f"{self.name} is member  of parent class 1")
        super().info()



class Parent2 : 
    def __init__(self,name) :
        self.name = name


    def info(self) : 
        print(f"{self.name} is member of parent class 2")


class Child(Parent1,Parent2) :
    def __init__(self,name) :
        super().__init__(name)


    def info(self):
        print(f"{self.name} is member of child class")
        super().info() 


obj = Child("Xyz")
obj.info()







# This situation is handled by MRO (Method Resolution Order) in Python.

# When both parents have the same method name, 
# Python decides which one to execute using left-to-right
# order defined in the child class.