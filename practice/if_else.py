age =input("enter your age\n")
age=int(age)
# print(type (age))
if (age>18):
    print('adult')
elif(age==18):
    print("perfect age")    
else:
    print('kid')    

# short hand if else
a=330
b=3303
print("A") if a>b else print('=') if a==b else print("B")

c=9 if a>b else 0
print(c)