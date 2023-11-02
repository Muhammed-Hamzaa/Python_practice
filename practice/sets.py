#sets are like lists but can't have repeated value 
#and no gurantee of order in output 
#can't access it's elements by index

s={2,3,'Carla',False,9,9}
print(s) 
print(type(s))

#empty dictionary
hamza={}
print(type(hamza))

#for empty set
info=set()
print(type(info))

for value in s:
    print(value)
print('----------')
a={1,2,3}
b={1,4,8,2,3}

#setname.add() -> if want to add a single item in a set
#setname.update() -> if u want to update more than one value
#setname.remove() ->to remove items from set and throws an error if not in set
#setname.discard() ->to discard  items from set and it does not throws an error if not in set
#setname.pop() ->to remove a random item from set
#del setname ->deletes the set *it is not a method but a keyword
#setname.clear ->deletes all the items in a set
#to check if a set contains values which another set consists
print(a.issubset(b))

#to check if a set contains some values including all the values of another set
print(b.issuperset(a))

#to check if there is not an intersection(common values) between sets
print(a.isdisjoint(b))

d=a.difference(b)
print(d)

#to get uncommon values of a set
c=a.symmetric_difference(b)
print(a,b,c)


#for union and intersection in sets
print(a.union(b))
print(a.intersection(b))
print(a,b)


#to add values of b into a
a.update(b)
print(a,b)

#to update a set with common values
a.intersection_update(b)
print(a,b)

