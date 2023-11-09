# In Python, is and == are both comparison operators that can be used to check if two values are equal. 
# However, there are some important differences between the two that you should be aware of.
a = [1,2]
b = [1,2]
# as lists are mutable both wil be true
print(a is b) # exact location of object in memory
print(a == b) # value
print('\n')

a= (1,2)
b= (1,2)
# as tuples are immutable both wil be true
print(a is b) # exact location of object in memory
print(a == b) # value