#find the duplicates in an array
lis=list(map(int,input().split()))
lis2=[]
for i in lis:
    if i not in lis2:
        lis2.append(i)
    else:
        print(i,end=" ")
#print(lis2)