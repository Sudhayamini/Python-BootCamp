import math
n=int(input())
val=0
for i in range(2,(int(math.sqrt(n))+1)):
    if n%i==0:
        val+=1
        break
if(val==1):
    print("is not prime")
else:
    print("is prime")


'''
n=int(input())
r=int(n**0.5)
count=0
for i in range(2)
'''