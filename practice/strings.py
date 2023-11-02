# strings slicing
fruit='Mango'
print(len(fruit))
# index of -1 means lenght of string-1
print(fruit[-1])
print(fruit[:-1])
print(fruit[-2:])

print(fruit[0:4])  #includes 0 but not 4
name="    ! Hamza !!!"
print(name[-4:-2])

# Strings are immutable
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.replace("a", "A")) 
print(name.strip(" ")) 
print(name.rstrip("!")) 
print(name.split(" "))

str='Hamza'
print(len(str))
print(len(str.center(50)))
print(str.center(50))
print(str.count('a'))
print(str.endswith('za'))
print(str.find('a'))
print(str.index("z"))
str='Affa    Ffs             a00\n'
print(str)
#retuns true if alphanumeric
print(str.isalnum())
#returns true if only alpha
print(str.isalpha())
#returns true if only printable characters
print(str.isprintable())
#returns true if wide spaces
print(str.isspace())
#returns true if all the first letters are capital
print(str.istitle())
# convert in to title
print(str.title())
#swap upper to lower and vice versa
print(str.swapcase())


name1= "              name1 "
name2='naMe2'

           # only triple quotes allow us to wite in next line 
name3='''HMZ
aka name3'''

print(name1)
print(name2)
print(name3[:3])

print(name1.strip())      #for removing spaces
print(len(name1))

print(name2.replace("2", "4"))

str1="this is a "
str2="concatenated string"

print(str1+str2)

p1="placeholder1"
p2="placehloder2"

temp= "{1} is a good boy and {0} is a bad boy.".format(p1,p2)
print(temp)

#  or from python 3.6 onwards we can use f string
temp=f"{p1} is a good boy and {p2} is a bad boy."

print(temp)



