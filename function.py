#function is a reusable block of code that performs a specific task. 

#scope of variable
#variables can have different scopes like 
#local scope: variable defines a within a function are local to that function and can only be accessed within that function
def myfunction():
    x=10 #x is a local variavle
    print(x)
myfunction()

y=20 # y is a global variable
def my_functon():
    print(y)
my_functon()

#non-local scope: if you want to modify a global variable from a within a function ypou can use a global key word to indicate
#that you are woking 

x=100
def modify_global():
    global x
    x=99
    print(x)
modify_global()
#--example com--#
#code start#

import random
def guess_number():
    return random.randint(1,100)
target_number=guess_number()
attempts=0
while True:
    user_guess=int(input("guess a number"))
    attempts+=1

    if user_guess==target_number:
        print(f"congratualtions!you won the game in {attempts} attempts")
        break
    elif user_guess<target_number:
        print("try a higher number")
    else:
        print("try a lower number")
#--code end--#
#--code-2--#
