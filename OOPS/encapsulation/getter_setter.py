class Employee :
    def __init__(self,name,salary) :
        self.name = name              #public member
        self.__salary = salary         #private member
        
    def get_salary(self) :            #getter method
        return self.__salary
    

    def set_salary(self,update_salary) :      #setter method
        self.__salary += update_salary


    # def info (self) :
    #     print(self.name , "salary is " , self._salary)  #accessed by method

detail =  Employee("XYZ" ,  50000 )
print(detail.get_salary())
detail.set_salary (15000)

print(detail.get_salary())
