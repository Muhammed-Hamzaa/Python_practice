a = input("enter a number between 5 and 9")

if(int(a)<5 or int(a)>9 ):
    raise ValueError('value should be between 5 nad 9')