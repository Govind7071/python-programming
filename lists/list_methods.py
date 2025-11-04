list=[2,1,3]
list.append(4)  #add one element at last position
print(list)
list.sort()  #sorts the list in ascending order permanently
print(list)  
list.sort(reverse=True)   #sorts the list in descending order permanently
print(list)  
list.reverse()    #reverse only the list at its corresponding index
print(list)
list.insert(2,5)   #insert element at  any index
print(list)
list.remove(2)  #removes first occurance at index
print(list)
list.pop()   #removes the element from last index
print(list)
list.pop(1)  #removes the element from particular index
print(list)
del list[0]
print(list)