#program to determine whether the number is armstrong or not
import math

def order(n):
    len=0
    while n!=0:
        len += 1
        n=n//10
    return len

def isArmstrong(n):
    x=order(n)
    temp=n
    sum=0
    while temp!=0:
        r=temp%10
        sum=sum+math.pow(r,x)
        temp=temp//10
    if sum==n:
        return 1
    else:
        return 0

n=int(input("Enter a number:"))
if isArmstrong(n)==1:
    print("{} is an armstrong number".format(n))
else:
    print("{} is not an armstrong number".format(n))
