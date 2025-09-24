vowels=['a','e','i','o','u']
print(vowels)
print(vowels[0])#to access elements index is required
print(vowels[0].title())#first element
print(vowels[-1])#to acces last element
names=['g1','g2','g3','g4']
a=int(input('input the index'))
print(names[a])
print('hii',names[a])
#modify elements in lists
motorcycles=['honda','yahama','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)#add new element
motorcycles.append('shine')
print(motorcycles)
print(motorcycles[3])