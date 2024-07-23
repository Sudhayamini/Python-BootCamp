'''a=10
b=12
a=a+b
b=a-b
a=a-b
print(a,b)'''
'''n=int(input())
print((n*(n+1)//2))'''
li=list(map(int,input().split()))
li.sort()
for i in range(len(li)-1,1):
    print(li[i])
