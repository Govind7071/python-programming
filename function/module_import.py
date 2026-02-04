import fuction_module    #Importing an Entire Module


total=fuction_module.sum_(2,3,4,5)
print(total)



from fuction_module import product       #Importing Specific Functions

mul=product(2,3,4)
print(mul)


from fuction_module import product as mul   #Using as to Give a Function an Alias

multiply=mul(4,5,6)
print(multiply)




import fuction_module as fm     #Using as to Give a Module an Alias

total=fm.sum_(1,2,3,4,5)
print(total)