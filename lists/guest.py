guest=[]
a=input("enter first guest name :")


b=input('enter second guest name:')

c=input('enter third guest name:')
guest.append(a)
guest.append(b)
guest.append(c)
print('you are invited to dinner ',guest[0])
print('you are invited to dinner ',guest[1])
print('you are invited to dinner ',guest[2])
print(guest.pop(1),'is not availabe for dinner')
d=input('enter other guest:')

guest.insert(1,d)
print(guest)
