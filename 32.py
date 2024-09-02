'''remove all the brackets from the given algebraic exp'''
'''''s=input()
for i in s:
    if ord(i)!=ord('(') and ord(i)!=ord(')') and ord(i)!=ord('{') and ord(i)!=ord('}') and ord(i)!=ord('[') and ord(i)!=ord(']'):
        print(i,end="")'''
#another method
'''n=input()
for i in n:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==99 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
print()'''
#HOMEWORK

# ABC,4 print EFG
s=input()
n=int(input())
for i in s:
    v=chr(ord(i)+n)
    print(v,end="")

