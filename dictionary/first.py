info={
    'name':'Govind',
    'branch':'CSE',
    'sec':18
}
print(info)
print(type(info))
print("my name is" ,info['name'])
info["name"]="Govind Yadav"          #assign new value
print("my name is" ,info['name'])  
info['sgpa']=8
print(info) #adding new key pair
print(info.get('name', 'No point value assigned.'))
