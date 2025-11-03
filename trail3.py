my_num = int(input("Enter a number: "))
guess = 0
while guess ** 2 < my_num:
    guess += 1 
if guess ** 2 == my_num:
    print(f"{my_num} is a perfect square")
else : 
    print(f"{my_num} is not a perfect square")