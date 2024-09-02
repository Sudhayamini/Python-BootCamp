#check how many vowels are there in a string
'''n=input()
count=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(count)'''
#or
n=input()
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
count=0
cnt=0
for i in n.lower():
    if(i in check):
        count+=1
    elif(i in abc):
        cnt+=1
print(count)
print(cnt)

# w a p to print all the cons