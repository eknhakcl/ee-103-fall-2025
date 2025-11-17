# from def_trail import is_even
# i = int(input("Enter a number: "))
# print(is_even(i))

# from def_trail import div_by
# a = int(input("Enter numerator: "))
# b = int(input("Enter denominator: "))
# result = div_by(a, b)
# print(f"Result: {result}")

# from def_trail import is_even
# for i in range ( 1,11):
#     if is_even(i):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

from def_trail import sum_odds 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = sum_odds(a, b+1)
print(f"Result: {result}")
