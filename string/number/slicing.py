string="0123456789"
print(string[0:])
print(string[1:5])
print(string[::-1])
print(string[0:9:2])
print(string[0::])
string="1,2,3,4"
print(string.split(",")) #string to list
list=["car","bus","motorcycle"]
print(" ".join(list))   #list to string
print(r"hii\thello")    #raw strings (no effect of \t,\n) 
print(r"hii\nhello")     #useful in c drive (jha file ka path ho)
print("hii\\hello\\")    #without raw string the o/p is differnet
print(r"hii\\hello\\")   #the o/p is same as given
