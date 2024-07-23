#peak element
#by checking adjacent 
'''lis=list(map(int,input().split()))
for i in range(1,len(lis)):
    if(lis[i]>lis[i-1] and lis[i]>lis[i+1]):
       print(lis[i],end=" ")
       break
    elif(lis[0]>lis[len(lis)-1]):
       print(lis[0])
       break
    else:
       print(lis[len(lis)-1])
       break'''
# another methods
'''lis=list(map(int,input().split()))
count=0 
for i in range(1,len(lis)-1):
   if(lis[i]>lis[i-1] and lis[i]>lis[i+1]):
      count=i
if(lis[-1]>lis[i-1] and lis[i]>count):
       count=len(lis)-1
print(lis[count])
#print(lis[i],end=" ")'''
#all peak
lis1=list(map(int,input().split()))
for i in range(1,len(lis1)):
    if(lis1[i]>lis1[i-1] and lis1[i]>lis1[i+1]):
        print(lis1[i],end=" ")
        
