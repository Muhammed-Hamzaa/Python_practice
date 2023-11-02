x=int(input('Enter the value of x: '))
match x:
    case 0:
        print('is zero')
    case 2:
        print('is two')
    case _ if (x!=90):
        print('not 90')
    case _ if (x!=80):
        print('not 80')
    case _:
        print('default case')
