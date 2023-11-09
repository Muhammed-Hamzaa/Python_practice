# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence.
# These functions are known as higher-order functions, as they take other functions as arguments.

# MAP 
def cube(x):
  return x * x * x

l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#   newl.append(cube(item))
newl = list(map(lambda x: x*x*x, l))
print(newl)



# FILTER
def filter_function(a):
  return a>2
  
newnewl = list(filter(filter_function, l))
print(newnewl)



# REDUCE
from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5] 
# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)
# Print the sum
print(sum)