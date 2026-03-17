n = int(input("enter the no. of processes"))

BT = []
AT = []
temp = []
WT = []
TAT = []
CT = []

avg_wait = 0
avg_TAT = 0
sum = 0



for i in range (1,n+1) :
    t = int(input(f"enter the arrival time of p{i}"))
    AT.append(t)
    
    t2 = int(input(f"Enter the brust time of p{i}"))
    BT.append(t2)


# print(AT)

# print(BT)

sort = sorted(zip(AT,BT))
new_l1,new_l2 = map(list,zip(*sort))


# print(new_l1)
# print(new_l2)

for i in new_l2 :
    sum = sum + i 
    CT.append(sum)



# print(WT)
for i in WT :
    avg_wait = i + avg_wait 


avg = avg_wait/len(WT)
print(avg)