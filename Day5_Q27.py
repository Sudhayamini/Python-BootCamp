#print all the vowels follwed by consonants
n=input()
n=n.lower()
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
for i in n:
    if(i in check):
        print(i,end="" )
for i in n:
    if(i in abc):
        print(i,end="")