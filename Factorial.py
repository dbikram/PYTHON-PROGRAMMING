# Factorial of a number
num=int(input("Enter a number:"))
f=1
for i in range(3,0,-1):
    f=f*i
print("The factorial of",num,"is",f)