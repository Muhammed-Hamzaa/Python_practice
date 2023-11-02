# pythonn 3.7 onwards dictionaries are ordered
dict={
    2:'hamza',
    3:'ali',
    4:'hafsa',
    5:'rehma'
}

print(dict[2])
print(dict.get(2))

print(dict.get(1))
#if u want error
# print(dict[1])

dict1 ={
    "Name":'Hamza',
    "age":21,
    "City": "karachi"
}
print(dict1)
print(dict1.keys())
print(dict1.values())

for key in dict1.keys():
    print(f'The value that corresponds to the key {key} is {dict1[key]}')

print('\n')
for key,value in dict1.items():
    print(f'The value that corresponds to the key {key} is {value}')

#dictionary methods
emp1={122:45,111:66,666:65}
emp2={333:64,339:89,121:90}

emp1.update(emp2)
print(emp1)

emp1.pop(122)
print(emp1)

emp1.popitem()
print(emp1)

del emp1[333]
print(emp1)