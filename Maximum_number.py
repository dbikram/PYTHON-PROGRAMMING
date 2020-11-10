# Maximum of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a>b:
    m=a
else:
    m=b
print("The maximum number of {0} and {1} is {2}".format(a,b,m))