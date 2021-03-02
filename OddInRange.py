#program to find all odd number in range
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
print("The odd numbers from {} to {} are:".format(start,end))
for i in range(start,end+1):
    if i%2!=0:
        print(i,end=' ')
