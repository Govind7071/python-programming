#add your favourite foods
#add elements in last position
food=[]
a=input("food 1:")
food.append(a)
b=input("food 2:")
food.append(b)
c=input("food 3")
food.append(c)
d=input("food 4")
food.append(d)
e=input("food 5")
food.append(e)
print(food)


#add elements to any positon
food.insert(2,"chocolate")
print(food)
vowels=['a','e','i','o','u']
vowels.pop()#remove last element
print(vowels)
vowels.pop(2)#remove elements from any index
print(vowels)