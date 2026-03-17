#use a property decorator in the car class to make the model attribute read only



class Car :
    def __init__(self,name,model):
        self.name  = name
        self.__model = model 

    @property
    def model (self) :
        return self.__model
    



my_car = Car ("Nexon","Tata")
# my_car.model ="Xyz"
# print(my_car.model())
print(my_car.model)