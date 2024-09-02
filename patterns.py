# print the following patterrn
'''
*****
*****
*****
*****
*****
'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end="")
    print()'''
#print the following pattern
'''
 ****
* ***
** **
*** *
**** 
'''
'''n= int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            print(" ",end="")
        else:
            print('*',end="")
    print()'''
# print the upper triangle
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end=" ")
    print()'''

#print the lower triangle

'''n=int(input())
for i in range(n):
    for j in range(n-i): 
        print('*',end=" ")
    print()'''


#print the number pyramid
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()'''
#print the parallelogram
'''n=int(input())
for i in range(1,):'''



#print the diagonal
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('*',end="")
        else:
            print(" ",end="")
    print()