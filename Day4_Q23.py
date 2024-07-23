#print the leap years in the given range
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%400==0 or (i%4==0 and (1%100!=0))):
        print(i)