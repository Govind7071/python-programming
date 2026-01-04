def factorial(n):
    if n==1 or n==0:
        return 1
    else :
        return n*factorial(n-1)
    

n=int(input("enter a number : "))
if n<0:
    print("factorial is not for negative number")
else:
    print("the factorial is",factorial(n))