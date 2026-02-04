current_username=["mohan","rohan","rakesh","akash","aman"]
new_users=["shyam","mukesh","AKASH","rakesh"]
current_user=[user.upper() for user in current_username]

for user in new_users :
    if user in current_username :
        print("the username is already used")
    elif user in current_user :
         print("the username is already used")
    else:
        print("the username is available")