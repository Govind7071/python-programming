class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x},{self.y}>"
    
    def eucleadanDistance(self,other):
        return ((self.x - other.x)**2 +(self.y - other.y)**2)** 0.5
    
    def distanceFromOrigin(self):
        return ((self.x )**2 + (self.y) **2)** 0.5
    
class Line :
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C}"
    
    def pointOnLine(line,point):
        
        if line.A*point.x +line.B*point.y+ line.C == 0 :
            return f"<{point.x},{point.y}> satisfies the line"
        return f"<{point.x},{point.y}> not satisfies the line"
    
    def shortestDistance(line,point):
        return abs((line.A*point.x +line.B*point.y +line.C)/(point.x **2 + point.y **2) ** 0.5)
    
    def intersectLines(self,line):
        if self.A /line.A != self.B/line.B :
            return "intersecting lines"
        
        return "not intersecting lines"



p1 = Point(2,3)
p2 = Point(3,2)
p3 = Point(1,-2)
print(p1.eucleadanDistance(p2))

print(p1.distanceFromOrigin())

l1 = Line(2,3,4)
print(l1)
print(l1.pointOnLine(p3))
print(f"{l1.shortestDistance(p1) :.2f}")

l2 = Line(2,3,1)     #l2 is reference varable holds the object  
l3 = Line(4,5,2)
print(l2.intersectLines(l3))
l4 = l3        #assign a new variable to existing object (does not create new object)
print(id(l3))  #both will point the same memory reference so make changes in any refelect to other 
print(id(l4))
