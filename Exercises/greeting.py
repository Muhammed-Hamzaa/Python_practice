import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
hour=int(input('Enter hour: '))
print(hour)

if(hour>=6 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<18):
    print("Good Afternoon!")
elif(hour>=18 and hour<20):
    print("Good Evening!")
elif(hour>=20 or hour<6 ):
    print("Good Night!")