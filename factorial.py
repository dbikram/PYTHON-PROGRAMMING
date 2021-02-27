def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        c=1
        while n>1:
            c=c*n
            n=n-1
        return c

n=int(input("Enter a number:"))
print("The factorial of {} is {}".format(n,fact(n)))
