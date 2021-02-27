#find the maximum element in the list
L=[]
n=int(input("Enter the number of element:"))
for i in range(0,n):
    L.append(int(input("Enter the list element:")))
res=max(L)
print("The maximum element in the list is:",res)
