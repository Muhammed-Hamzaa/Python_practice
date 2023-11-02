# enumerate function

marks =[1,2,43,99,66,81]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print('Awesome!')
#     index +=1

#same output as above using enumerate function
# tuple unpacked
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print('Awesome!')

# for index,mark in enumerate(marks,start=1):
#     print(mark)
#     if(index==3):
#         print('Awesome!')

#returns a tuple in format (index,mark)
# for v in enumerate(marks):
#     print(v)
#     if(v==3):
#         print('Awesome!')
    