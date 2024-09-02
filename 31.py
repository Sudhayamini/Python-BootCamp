# w a pto print all the capital letters in given string
n=input()
str=""
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        str+=(i)
print(str)