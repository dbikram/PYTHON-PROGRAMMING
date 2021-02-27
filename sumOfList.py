#program to find the sum of list element
def Sum(L):
    x=0
    for i in L:
        x=x+i
    return x
L=[]
n=int(input("how many elements,do you want to insert in the list:"))
for i in range(0,n):
    L.append(int(input("Enter the element:")))
res=Sum(L)
print("The sum of list element:",res)
