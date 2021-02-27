n=int(input("Enter the fibonacci term:"))
a=-1
b=1
print("The fibonacci series upto {} term".format(n))
for i in range(0,n):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
