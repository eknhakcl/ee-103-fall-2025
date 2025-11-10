x= input("Enter operation (add, subtract, multiply, divide): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def calculate(x , num1 , num2):
    if x == "add":
        return num1 + num2
    elif x == "subtract":
        return num1 - num2
    elif x == "multiply":
        return num1 * num2
    elif x == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print(f"The result is: {calculate(x, num1, num2)}")

import pdb; pdb.set_trace() 