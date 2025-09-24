values=[]

for value in range(1,21):
   values.append(value)
print(values)
print(min(values))
print(max(values))
print(sum(values))
odd_num=[]
for odd in range(1,21,2):
   odd_num.append(odd)
print(odd_num)

multiple=[value*3 for value in range(1,11) ]
print(multiple)
   
cube=[value**3 for value in range(1,11)]
print(cube)
   
