#Remove empty list from a list
l=[1,2,3,4,[],5,6,[],7,8,[],9,10]
for i in range(len(l)):
    if(l[i]!=[]):
        print(l[i],end=' ')
