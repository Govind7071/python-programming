# Hybrid inheritance is a combination of more than one type of inheritance.


class Person :
    def __init__(self,name) :
        self.name = name 


class Teacher(Person) :
    def info(self) :
        print(self.name ,"is a teacher")

class Subject :
    def __init__(self,sub) :
        self.sub = sub      


class Dept(Teacher,Subject) :
    def __init__(self,name,sub) :
        Person.__init__(self,name)
        Subject.__init__(self,sub)

    def info(self) :
        print(f"{self.name} is the teacher who teaches {self.sub}")


detail = Dept("Mr","Python")


print(isinstance(detail,Subject))
print(isinstance(detail,Person))
detail.info()
 
