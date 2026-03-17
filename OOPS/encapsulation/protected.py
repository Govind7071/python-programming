
#  protected members are defined with a single underscore prefix (e.g., self._name).


class Employee :
    def __init__(self,name,salary) :
        self.name = name              #public member
        self._salary = salary         #protected member

    def info (self) :
        print(self.name , "salary is " , self._salary)  #accessed by method


detail =  Employee("XYZ" ,  50000)
detail.info()