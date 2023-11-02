# funtions  
def greet():
    print('Good Morning\n')
    print('Good Afternoon\n')
    print('Good Evening\n')
    print('Good Night\n')

greet()    

#   ....................................
# def sum(a,b):
#     return a+b

# c=input('''enter the numbers you want to add
# 1. ''')
# d=input('2. ')


# c=int(c)
# d=int(d)

# print(sum(c,d))

# using pass to put the conditions later on so it dosen't throws an error
def isweak():
    pass

# function arguments
# 1.default argument ----  1 and 2 
def sum(a=1,b=2):
    print("Sum: ",a+b)

# 2.required argument ----  3 and 4
sum(3,4)

def cgpa(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print('Cgpa of ',len(numbers),' semesters is : ',sum/len(numbers))

cgpa(3.4,3.3,3.46,3.75) 

def name(**name):
    print(type(name))
    print('Hello my name is',name["fname"],name["mname"],name["lname"])

name(fname="Muhammad",lname="Ghia",mname="Hamza")