#list of elements count even and odd elements
'''
question 7.1

'''
'''li=list(map(int,input().split()))
even=0
odd=0
for i in range(len(li)):
    if(li[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)'''
        

#question 7.2
#you are given a comma seperated natural  from 1 to 10 print even numbers

'''li=list(map(int,input().split(",")))
for i in range(1,11,2):
        print(li[i],end=" ")'''
#this problem can be solved in this way
'''li=list(map(int,input().split(",")))
print(li[1:len(li):2])'''



