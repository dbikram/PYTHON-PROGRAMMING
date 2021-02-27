#program to find sum of square of first n natural numbers
import math
n=int(input("Enter the n th term:"))
sum=0
for i in range(1,n+1):
    sum=sum+math.pow(i,2)
print("The sum of square of first "+str(n)+" th term is",sum)
