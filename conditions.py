#condition checking
'''N=int(input())
if(N>0 and N%2==0):
    print("positive and even")
elif(N>0 and N%2!=0):
    print("positive and odd")
elif(N<0 and N%2==0):
    print("negative and even")
elif(N<0 and N%2!=0):
    print("negative and odd")'''
#question
''' mr z is selected for olympics he is participating in swimming competition only one
winner is selected in th e competition 
MR X mr y are friends of z mr x is part of badmint mr y in table tennies,
according to the selection committee the
require of badmintion
height 140 cmp
weight faactors of 2
body fat < than 12%
according to selection committee
require table tennies
height min 118 cm to 148cm
weight factors of no of medals won by mr z
body fat 14%
according to previous history z participated in 14 games out which he is hvaing success rate of 65%
write a program wheather to check mr x and mr y and mr z travalled in the same plane or not
'''
xh=int(input())
xw=int(input())
xbf=int(input())
yh=int(input())
yw=int(input())
ybf=int(input())
if xh>=140 and xw%2==0 and xbf<12:
    x=1
if yh>=118 and yh<=148 and yw%9==0 and ybf<=14:
    y=1
if x==1 and y==1:
    print("they are travelling in same plane")
else:
    print("they are not travelling in same plane")