
# private members are defined with a double underscore prefix (e.g., self.__salary)


class Employee :
    def __init__(self,name,salary) :
        self.name = name              #public member
        self.__salary = salary         #private member

    def info (self) :
        print(self.name , "salary is " , self.__salary)


detail =  Employee("XYZ" ,  50000)
detail.info()