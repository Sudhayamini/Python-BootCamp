#reverse the numbers in the given string 
#HOMEWORK
n=input()
digit="0123456789"
ans=""
for i in n:
    if i in digit:
        ans+=(i)
ans=int(ans)
while(ans>0):
    print(ans%10,end="")
    ans//=10
    


