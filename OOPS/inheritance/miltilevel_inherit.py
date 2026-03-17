# In multilevel inheritance, a class is derived from another derived class (like a chain).



class Student :
    def __init__(self,name) :
        self.name = name


class Section(Student) :
    def __init__(self,name,section) :
        super().__init__(name)

        self.section = section


class Rollno(Section) :
    def __init__ (self,name,section,rollno) :
        super().__init__(name,section)
        
        self.rollno = rollno

    def details (self):
        print(f"the student name is {self.name} from section {self.section} and roll number {self.rollno}")


detail = Rollno(name = "govind", section = 18, rollno = 474)

detail.details()