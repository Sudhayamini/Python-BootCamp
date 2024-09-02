class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
    
obj1=Myclass
v=obj1.add(2,5)
u=obj1.sub(2,5)
w=obj1.mul(2,5)
x=obj1.div(2,5)
y=obj1.mod(2,5)
print(v,u,w,x,y,end="")
