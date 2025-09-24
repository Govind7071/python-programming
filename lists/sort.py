#permanently sorting in lists


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()   #sort in alphabetical order
print(cars)
num=['1','3','5','9','7']
num.sort()    #sort in ascending order
print(num)
odd=['1','3','5','9','7']
odd.sort(reverse=True)     #sort in descending order
print(odd)


#temporary sorting of list


odd_num=['1','3','5','9','7']
#sorted(odd_num)
print(sorted(odd_num))#sorted list
print(odd_num)#original list