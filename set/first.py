 #set
num={1,2,3,4} 
print(num)
null_set=set()   #empty set
set={1,3,5,5,7,7,7,"hello",8,'hii'}
print(set)
print(len(set))
null_set.add(5)  #add an element
null_set.add((7,4,5)) 
null_set.add(9)   
print(null_set)
null_set.remove(9)  #removes the given element
print(null_set)
null_set.pop()     #removes the random value
print(null_set)
null_set.clear()   #empty the set
print(null_set)
print(type(null_set))