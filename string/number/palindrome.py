str='malayalam'
is_palindrome=True
for i in range(len(str)//2):
    if str[i]!=str[-(i+1)] :
        is_palindrome=False
        break
if is_palindrome:
    print("yes palindrome")
else:
    print("not palindrome")