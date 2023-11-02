# error handling if u don't want to halt the program
#instead error will be printed

a=input('Enter the number')
print(f"Times table for {a} is")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")

# except Exception as e:
except :
    print(f"invalid input: {a}")    

#both finally and the print will be executed but to see the difference of finally
#use the function to execute the whole process
# and u will see finally being executed whereas print below it will not be executed
finally:                              
    print('I am always executed')

print('I am always executed')

