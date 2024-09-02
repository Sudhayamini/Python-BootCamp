#i/p= hello-----world
#o/p=-----hello world
'''s=input()
check="-"
abc="abcdefghijklmnopqrstuvwxyz"
for i in s:
    if(i in check):
        print(i,end="" )
for i in s:
    if(i in abc):
        print(i,end="")'''
#another method
n=input()
count=0
ans=""
for i in n:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)