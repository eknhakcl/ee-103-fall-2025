x = int(input("Enter a number: "))
guess = 0.0
increment = 0.01
epsilon = 0.1

while guess **2 <x :
    guess += increment
    if abs(guess**2 - x) < epsilon :
        print(f"{guess} is close enough to the square root of {x}")
        break
    else :
        pass
