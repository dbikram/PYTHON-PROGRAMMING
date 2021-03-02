#program to Count the occurance of the element in a list
def occurance(l,x):
    count=0
    for i in range(len(l)):
        if l[i]==x:
            count=count+1
    return count
        
l=[]
n=int(input("Enter the numbers of element:"))
for i in range(n):
    l.append(int(input("Enter the element:")))
x=int(input("Enter the number which is at the list:"))
a=occurance(l,x)
print("The occurance of {} is {}".format(x,a))
