'''
question 6
take a space separated input from a user and print alternate elements
'''
list1=list(map(int,input().split()))
for i in range(0,len(list1),2):
    print(list1[i],end=" ")