'''
in python polymorphism is not possible but can be achieved by using method over riding and method overloading
abstraction can be acheived by using abc moduleand abstract method
encapsulation is files bundled together and can be acheived by using access specifier(public private, protected)
method overloading compile time
method overriding run time 
'''
#variable length argument  is the best method for doing the method overloading
class Cal:
    def add(self,*args):
        return sum(args)
obj=Cal
print()