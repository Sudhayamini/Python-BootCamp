'''
given an space separated integer list in the average of elements in the even index
'''
lis=list(map(int,input().split()))
count=0
total=0
for i in range(0,len(lis)):
    if(i%2==0):
        count+=1
        total=total+lis[i]
print(total/count)

        
