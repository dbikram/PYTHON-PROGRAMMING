#program to print all even numbers in a range
start ,end =input("Enter the start and end:").split(' ')
start=int(start)
end=int(end)
for i in range(start,end+1):
    if i%2==0:
        print(i,end=' ')
