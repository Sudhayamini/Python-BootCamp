#lcm and gcd
a,b=map(int,input().split())
x,y=a,b
while b!=0:
    a,b=b,a%b
print("gcd is",a)
print("lcm",x*y//a)

'''a,b=map(int,input().split())
if(a%b==0 or b%a==0):
    print(b)
else:
    print(a*b)'''
