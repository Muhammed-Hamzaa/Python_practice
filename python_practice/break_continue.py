# break continue statements

#break
for i in range(12):
    if(i==10):
        break
    print('5 x ',i," = ",5 *i)

print('loop exited')


#continue
for i in range(12):
    if(i==10):
        print('skipping iteration')
        continue
    print('5 x ',i," = ",5 *i)

# emulating do while loop 
i=0
while True:
    print(i)
    i=i+1
    if(i%10==0):
        break

