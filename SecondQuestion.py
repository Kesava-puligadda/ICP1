#Delete and Replace

string=input("enter the string")
print (string)
n=3
string[:-n]
print(string[:-n])
print(string[:-n][-1::-1])

#Arthimetic Operations

A=input('give the first number')
B=input('give the second number')

sum=float(A)+float(B)
Sub=float(A)-float(B)
Mul=float(A)*float(B)
Div=float(A)/float(B)

print('The sum of {0} and {1} is {2}'.format(A, B, sum))
print('subraction of {0} and {1} is {2}'.format(A,B,Sub))
print('Multiply of {0} and {1} is {2}'.format(A,B,Mul))
print('Divison of {0} and {1} is {2}'.format(A,B,Div))