import random
number=random.randint(1,100)
user_guess=None
attempts=0   
while number!=user_guess:
    user_guess=int(input("Guess the number: "))
    attempts+=1
    if number<user_guess:
        print("Too High")
    elif number>user_guess:
        print("too low")
            
print(f"Correct, no of attempts taken is {attempts}\nExit")