#program-1
age=27
if age>=10:
    print("you are an adult.")
else:
    print("you are not adult.")
#program-2
score=87
if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score<=70:
    grade="C"
print(grade)
#program-3
is_raining=True
is_cold=True
if is_raining:
    print("bring umbrella")
    if is_cold:
        print("wear a jacket")
else:
    print("nice weather to go out.")
#progam-4
number=10
if number>0:
    print("positive.")
elif number<0:
    print("negative.")
else:
    print("neutral")
#program-5
my_Set={1,2,3,4,5}
my_Set.add(6)
my_Set.add(7)
my_Set.add(8)
my_Set.add(9)
my_Set.remove(1)
print(my_Set)
#program-6
my={1,2,3,4,4,7}
my1={5,6,7,8,5,4,4}
inter=my.intersection(my1)
print(inter)
#program-7
#creating an object
class Dog:
    def _init_(self,name):
        self.name = name
        dog1 = Dog("bobby")
        print(dog1.name)
