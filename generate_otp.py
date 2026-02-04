import random
import time
 



otp=random.randint(100000,999999)

print(otp)


enter=input("enter the otp")
if enter==otp :
    print("successfully")

else :
    
    print("try again")