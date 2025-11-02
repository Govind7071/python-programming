str="i am a string"
print(len(str)) #function for length calculation
print(str[0])#index start from 0
print(str[2:8])#slicing:accessing a part of string
print(str[2:])#this will print to last index
print(str[:6])
print(str[-4:-1])#negative index stt from end and value -1
print(str.endswith("ing"))#returns True if string ends with substring
print(str.capitalize())#capitalize the first char
print(str.replace("string","STRING"))
print(str.find("am"))

print(str.count("a"))#counts the total number of occurance