class Car :
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    @staticmethod
    def general ():            #decorator
        print("i am class instance")
      



class Fuel_type (Car):

    def info(self):
        print("Petrol or diesel car")


class Electric_car (Car) :
    

    def info(self):
        print("Electric fuel")



car = Fuel_type("safari","tata")
car.info()


tesla = Electric_car("ty","tata")
tesla.info()

Car.general()