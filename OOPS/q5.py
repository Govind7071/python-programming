#Demonstrate polymorphism by defining a method fuel_type in both Car and ElecricCar classses,but with different behaviors.


class Car:
    def __init__(self,brand,model):
         self.__brand=brand      #_ _ makes the brand private
         self.model=model

    def get_brand(self):
         return self.__brand
    
    def full_name(self):
         return f"{self.__brand}:{self.model}"     #class ke log to brand ko access kr sakte hai 
    
    def fuel_type(self):
         return "petrol or diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size) :
         super().__init__(brand,model)
         self.battery_size=battery_size

    def fuel_type(self):
         return "electric charge"


my_tesla=ElectricCar("Tesla","model s","85kWh")
my_car=Car("tata","suv500")
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())

print(my_car.fuel_type())
print(my_tesla.fuel_type())