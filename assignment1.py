#Q1
a = int(input("enter your first number "))
b = int(input("enter your second number "))
c = int(input("enter your third number "))
average=a+b+c/3
print("The average of three number is",average)

#Q2
a=float(input("enter your income"))
b=a-10000
c=int(input("dependents"))
d=c*3000
e=b-d
f=(0.2*e)
print(f)

#Q3
s=int (input("Enter Seconds : "))
m=s//60
s=s%60
print(m,"minutes",s,"seconds")

#Q4
a=int(input("num ; "))
b=int(input("num2 ; "))
c=int(input("num3 ; "))
d=a+b+int(c)
print (d)

#Q5
import math
a= int(input("enter the value from 0-345 ; "))
b=print(math.sin(math.radians(a)),math.cos(math.radians(a)))