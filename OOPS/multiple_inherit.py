class Animal :
    def __init__(self,name) :
        self.name = name



class Name :
    def __init__(self,type) :
        self.type = type


class Another_name (Animal, Name) :

    def __init__(self,name,type ) :
        Animal.__init__(self,name)
        Name.__init__(self,type)

    def info(self) :
        print(self.name ,":::",self.type)
        


anim = Another_name("dog","german")

anim.info()