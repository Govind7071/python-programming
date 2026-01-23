file1=open("f1.txt","w")
list1=["hii\n","hello\n","this is govind"]
str="heyy"

# file1.write("HII")
# file1.close()
# file1=open("f1.txt","w")
# file1.write(str)
# file1.write(list1[0])
file1.write(str)
file1.writelines(list1)
file1.close()
file1=open("f1.txt","r")
print(file1.read())
file1.close()
