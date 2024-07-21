'''
replace the elements in an array with avg of max and min elements
'''
lis=list(map(int,input().split()))
maxi=0
mini=lis[0]
for i in lis:
    if(i>maxi):
        maxi=i

for j in lis:
    if(j<mini):
        mini=j
sumi=maxi+mini
print(sumi)
avg=sumi//2
for i in range(len(lis)):
    lis[i]=avg
print(lis)



