class Employee :
    def __init__(self,name,salary) :
        self.name = name              #public member
        self.salary = salary

    def info (self) :
        print(self.name , "salary is " , self.salary)


detail =  Employee("XYZ" ,  50000)
detail.info()