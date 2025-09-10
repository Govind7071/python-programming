#grade of a student
marks=int(input(" enter the marks :"))
if(marks>=90):
    print("A grade")
elif(marks>=80 and marks<90):
    print("B grade")
elif(marks>=70 and marks<80):
    print("C grade")
elif(marks>=60 and marks<70):
    print("D grade")
else:
    print("E grade")
    
var=5
print(var>3 and var<10)
print(var>3 or var<4)