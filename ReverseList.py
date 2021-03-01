l=[]
n=int(input("Enter the number of elements you want to insert into list:"))
for i in range(n):
    l.append(int(input("Enter the element:")))
l.reverse()
print("The reverse of the list is:",l)
