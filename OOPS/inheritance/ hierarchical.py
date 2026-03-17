# In hierarchical inheritance, multiple child classes inherit from the same parent class




class Person :
     

     def __init__(self,name) :
          self.name = name



class Teacher(Person) :
     def info(self) :
          print(f"{self.name} is teacher")


class Student(Person) :
     def info(self) :
          print(f"{self.name} is a student")




teacher_detail=Teacher("Mr Arvind")
teacher_detail.info()
student_detail=Student("Govind")
student_detail.info()

