#program to find the sum of cube of first n natural numbers
import math
n=int(input("Enter the n th term:"))
sum=0
for i in range(1,n+1):
    sum=sum+math.pow(i,3)
print("The sum of first "+str(n)+" th term is",sum)
