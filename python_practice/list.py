l=[5,6,8,4]
print(type(l))
if "Hamza" in l:
    print('yes it is')
else :
    print('not in list')    



lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if(i%2==0)]
print(lst)

l.append(7)
print(l)

l.reverse()
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

print(l.count(3))

#don"t use 
# m = l 
# instead use
m=l.copy()
m[0]=0
print(m)
print(l)

l.insert(1,44)
print(l)

l.extend(m)
print(l)

k=l+m
print(k)
