l=[]
n=int(input("Enter the number of elemenets you want to insert in list:"))
for i in range(n):
    l.append(int(input("Enter the element:")))
l.sort()
print("The second largest element is:",l[-2])
