def is_even(i):
    if i % 2 == 0:
        return True
    else:
        return False
    
def div_by(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def sum_odds(a,b):
    total = 0
    for i in range (a,b+1):
        if is_even(i) == False:
            total += i
    return total

def largest_num():
    return max(a,b,c)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))   
# c=int(input("Enter third number: "))
# result = largest_num()
# print(f"Largest number is: {result}")
