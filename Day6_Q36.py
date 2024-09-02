# multiple inheritance
class Father:
    def father_speak():
        return " im father"
class Mother:
    def mother_speak():
        return " im mother"
class Kid(Father,Mother):
    def kid_spaek():
        return " im kid i have properties of mother and father" 
obj=Kid
print(obj.kid_spaek())
print(obj.father_speak())
print(obj.mother_speak())

