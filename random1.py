import random
random_num = random.randint(-100, 100)
user_guess = int(input("Guess a number between -100 and 100: "))
if user_guess == random_num:
    print(":)")
else:
    print(f":( it was {random_num}")
