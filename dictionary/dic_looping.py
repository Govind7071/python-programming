dictionary={}
active=True


while active :
    name=input("enter your name : ")
    food=input("enter your favourite food : ")
    dictionary[name]=food

    repeat=input("would you like to another person detail ?(yes/no)")

    if repeat.lower()=="no" :
        active=False

print("\n---Poll Results---")
for name,food in dictionary.items() :
    print(f"{name} favorite food is {food}")
