info={
    'name':'Govind',
    'branch':'CSE',
    'subject': {
        'ds':12,
        'python':11,
        'maths':13.5
    }
}
print(info)   #to access complete dictionary
print(info['name'])    #to access particular key value
print(info['subject'])   ##to access particular key value
print("marks in maths is",info['subject']['maths'])  #to access  particular key in nested dictionary
for key,value in info.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
for information in (info.keys()):
    print(information.title())