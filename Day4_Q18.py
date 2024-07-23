#password verifier
'''
mr x is trying to create a new password for his insta account
these are the required conditions for creating a new 
1. min len is 8 and max 15
2. only @ and / are must
3.no spaces are allowed
4.only alpha numerics are allowed
you are supposed to print weak if len is exact 8, medium leng is bet 8 to 12, strong if len is 12 to 15
'''
pas=input()
var=len(pas)
count=0
str='@/'
if(var<8):
    print("enter minimum")
elif( var>15):
    print("limit exceeded")
for i in pas:
    if(i in str[0] or str[1] and i!=' '):
        count+=1
        break
if(count>1):
        print("must include special character")
elif(var==8):
    print("password is weak")
elif(var>8 and var<=12):
    print("password is medium")
elif(var>12 and var<=15):
    print("password is strong")