current_users=['a','b','c','d','e']

new_users=['a','A','E','f','g','p']
for new_user in new_users :
    if new_user.lower() in current_users:
        print("user already exist")
    else:
        print("the username is available")
# available_toppings = ['mushrooms', 'olives', 'green peppers',
# 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#       print(f"Adding {requested_topping}.")
#     else:
#        print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making your pizza!")