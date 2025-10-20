import random
random_num = random.randint(0, 100)
user_guess = int(input("Guess a number between 0 and 100: "))
if user_guess == random_num:
    print(":)")
else:
    print(f":( it was {random_num}")
