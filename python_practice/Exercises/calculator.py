'''
Arithnetic operatrs
+  add
-  subtract
*  multiply
/  divide
%  modulus
// floor division
** exponential
'''
print("      *** CALCULATOR ***")
print('Enter two numbers')
a=float(input('First Number: '))
b=float(input('Second Nmber: '))
c=float(input('''Select the operator:
(1) +  add
(2) -  subtract
(3) *  multiply
(4) /  divide
(5) %  modulus
(6) // floor division
(7) ** exponential\n'''))
if c==1:
 print(a," + ",b," = ",a+b)
elif c==2:
 print(a," - ",b," = ",a-b)
elif c==3:
 print(a," * ",b," = ",a*b)
elif c==4:
 print(a," / ",b," = ",a/b)
elif c==5:
 print(a," % ",b," = ",a%b)
elif c==6:
 print(a," // ",b," = ",a//b)
elif c==7:
 print(a," ** ",b," = ",a**b)
else:
 print("invalid operater input")
