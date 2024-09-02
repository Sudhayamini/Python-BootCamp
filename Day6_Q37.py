#single in heritance
class Automoblie:
    def engine():
        return "automoblies "
class Car(Automoblie):
    def parts():
        return " car has engine"
obj1=Car
print(obj1.engine())
print(obj1.parts())
