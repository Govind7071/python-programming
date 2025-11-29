from first import info
print(info.keys())  #returns all the keys
# list=[]
# a=int(input())
# list.append(a)
# a=int(input())
# list.append(a)
# sum=0
# for i in list[0:]:
#    sum=sum+i
# print('sum =',sum)
print(info.values()  ) #reutrns all values
print(info.items())     #returns all(keys,values) pairs as tuples
print(info.get("sgpa"))  #returns the key's value
info.update({'sem':2})   #insert the specific key:value to the dictionary
print(info)
