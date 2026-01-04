# check if a password is weak, medium or strong .Criteria:<6chars (weak),6-10chars (Medium),10chars (strong)
password=input("enter a password : ")
length=len(password)
if length<6:
    print("Password is weak")
elif length<10:
    print("password is medium")
else :
    print("Password is strong")