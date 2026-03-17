class Student :
    def __init__(self,name) :
        self.name = name


    


class College (Student) :
    def info(self) :
        print(self.name ,"is a student of ABES")



class Roll (College) :
    def roll(self,roll) :
        print(f"Roll no of {self.name} is {roll}")



details = Roll("Govind")
details.info()
details.roll(474)


# Bachcha (child) maa-baap (parent) ki cheezein use kar sakta hai,.....
# par maa-baap bachche ki cheezein use nahi kar sakte.



# __init__ likha = ❌ parent ka gate band

# super() likha = ✅ gate khola


    