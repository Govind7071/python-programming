def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True
string=input("enter a string : ")
if is_palindrome(string) :
    print(string,"is palindrome")
else :
    print(string,"is not palindrome")