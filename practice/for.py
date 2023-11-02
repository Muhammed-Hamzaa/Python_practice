# for loop
name='Muhammad'
print(name)
for x in name:
    print(x)

colors =['Red','Green','Blue']
for color in colors:
    
    print(color)
    for i in color:
        print(i)
print('\n')
# in range start, stop, step
for k in range(1,10,2):
    print(k)
#            times table

# num=int(input('Enter a number u want mutiples of: '))
# start=int(input("starting with: "))
# stop=int(input("ending with: "))
# for i in range(start,stop+1):
#     print(num," x ",i," = ",num*i)

# python allows else to be used in for and while loops if loop breaks not completed

#else not executed

for i in range(4):
    print(i)
    if i==3:
        break
else:
    print('Sorry no i')   

#else will execute
for i in []:
    print(i)
else:
    print('Sorry no i')    

i=0
while i<7:
 print(i)
 i=i+1
else:
    print('out of loop')

