'''my_list=[1,2,3,4]
print(*my_list)
# '*' is used for removing commas and square brackets
#print(my_list)''' #methods in the list
'''my_list.append(776) #appends at last
print(my_list)
my_list.insert(0,77) #inserts at 0th index and insterted position should be given
print(*my_list)
print(len(my_list)) #prints the length of the list
my_list.pop()
print(*my_list) #by default pops the list element
my_list.pop(0) #delets the 0th index
print(*my_list)
my_list_2=[5,6,7,8]
new_lst=my_list+my_list_2
print(*new_lst)
new_lst=my_list.copy()
print(*new_lst)
new_lst.pop()
print(*new_lst)
cnt=my_list.count(2) #counts the no of occurrences of the element
print(cnt)
my_lst3=[2,66,77,3,5,9]
my_lst3.sort() #sorts the elements in the list and modifies the original list
#time complexity is (nlogn)
print(*my_lst3)'''
#taking list dynamically
'''my_list=list(map(int,input().split(",")))
 #list type casting,  map-> more than one element, int-> data type, input->function, 
 # split()for space separator or defaultly uses spaces/ we can use anything in between as well eg: '@',','
print(*my_list)'''
print("enter the list values")
list1=list(map(int,input().split(" ")))
print("enter 1 for append")
print("enter 2 for pop")
print("enter 3 for sort")
print("enter 4 for hello length")
choice=int(input())
if(choice==1):
    print("enter the element to appended")
    list1.append(int(input()))
    print(*list1)
elif(choice==2):
    list1.pop()
    print(*list1)
elif(choice==3):
    list1.sort()
    print(*list1)
elif(choice==4):
    print(f"hello length of list is {len(list1)}")
    
