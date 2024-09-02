#multilevel inheritance
class Animal:
    def Speak():
        return " Animal is "
class Dog(Animal):
        def Bark():
            return " Bow..."
class Puppy(Dog):
     def puppy_speak():
          return " im puppy :))"

obj1=Animal
obj2=Dog
obj3=Puppy
print(obj1.Speak())
print(obj2.Bark())
print(obj3.puppy_speak())
