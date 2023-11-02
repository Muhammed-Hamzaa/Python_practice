# tuples can't be changed
t = (1,2,4,5,55,34,4)
print(type(t))
print(len(t))
# u can change tuple indirectly by coverting it into a list
temp = list(t)
temp.append(6666)
t=tuple(temp)
print(t)

#index(element,start,end)
i=t.index(4,3,7)
print(i)