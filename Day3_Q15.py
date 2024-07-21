#find the missing number in an array
lis=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(1,11):
    sum1+=i
for i in range(len(lis)):
    sum2+=lis[i]
missno=sum1-sum2
print(missno)