# create a function that returns, both the area and circumference of a circle given its radius
# import math
# def area(radius):
#     area=math.pi *radius**2
#     return area
# def circumference(radius):
#     circumference=2*math.pi*radius
#     return circumference
# radius=float(input("enter the radius of circle : "))
# print(f"the circumference is {circumference(radius):.3f} and the area is {area(radius):.3f}")


 #method 2
import math
def circle(radius):
    area=math.pi*radius**2
    circumference=math.pi*2*radius
    return area,circumference
radius=float(input("enter the radius of circle : "))
area,cir=circle(radius)
print(f"the area of circe is {area:.3f} and the circumference is {cir:.3f}")