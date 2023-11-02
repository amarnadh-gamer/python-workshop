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