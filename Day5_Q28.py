# print the unique characters in a string
'''n=input()
ns=""
for i in n.lower():
    if i not in ns:   #n.count(i)==1               
        ns+=i
print(ns)'''

# hello123world o/p =6
'''n=input()
abc="abcdefghijklmnopqrstuvwxyz"
digit="0123456789"
sum=0
for i in n:
    if i in digit:
        sum+=int(i)
print(sum)'''

#using ascii values as range
n=input()
sum=0
for i in n:
    if ord(i)>48 and ord(i)<=57:
        sum+=int(i)
print(sum)

