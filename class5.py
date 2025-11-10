# guess and check

# my_num = int(input("Enter a number: "))
# guess = 0
# while guess ** 2 < my_num:
#     guess += 1 
# if guess ** 2 == my_num:
#     print(f"{my_num} is a perfect square")
# else : 
#     print(f"{my_num} is not a perfect square")

# apporoximation method

# increment = 0.01
# epsilon = 0.1
# x= int(input("Enter a number: "))
# guess= 0.0

# while guess**2 < x+10 :
#     guess += increment
#     if abs(guess**2 - x) < epsilon :
#         print(f"{guess} is close enough to the square root of {x}")
#         break
#     else :
#         pass

# bisection search
x= 15
epsilon = 0.01
increment = 0.001
low = 0.0
high = x
guess = (high + low) / 2
num_guesses = 0

while abs(guess** 2 - x) >= epsilon :
    print(f"Low value is {low}, high value {high}.")
    if round(low ,2) == round (high , 2):
        print(f"{x}'s squareroot is approxamitly {high}")
        break
    else:
        if guess**2 > x:
            high = guess
        elif guess**2 <x :
            low = guess
        guess =(high + low)/2

