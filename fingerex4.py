import math
n = float(input("Enter a number: "))
n = math.sqrt(n)
if n == int(n):
    print("Perfect square")
else:
    print("Not a perfect square")