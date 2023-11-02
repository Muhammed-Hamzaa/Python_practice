
num=int(input('Enter a number u want mutiples of: '))
start=int(input("starting with: "))
stop=int(input("ending with: "))
for i in range(start,stop+1):
    print(num," x ",i," = ",num*i)