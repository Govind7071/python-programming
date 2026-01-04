#Add a class variable to Car that keeps track of the number of cars created.
input_string="mohan"
output_string="mohai"
my_list=[]
op_list=[]
result=[]
# for c in range(len(string)):
#     my_list.append(string[c])
# # print(my_list)
# for c in range(len(string)):
#     op_list.append(output[c])
# # print(op_list)



# for item in my_list:
#     if item not in op_list:
#         result.append(item)
# for item in op_list:
#     if item not in my_list:
#         result.append(item)
# print(result)
for ch in input_string:
    if ch not in output_string :
        result.append(ch)
for ch in output_string:
    if ch not in input_string:
        result.append(ch)
print(result)