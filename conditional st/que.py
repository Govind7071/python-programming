# movie tickets are based on age $12 for adult(18 and over) , $8 for children. Everyone gets a $2 discount on Wednesday.
age=int(input("enter the age : "))
day=input("enter the day : ")
price=12 if age>=18 else 8
   
if "wednesday"==day.lower() :
    print(f"the movie ticket is ${price-2}")
else:
    print(f"the movie ticket is ${price}")