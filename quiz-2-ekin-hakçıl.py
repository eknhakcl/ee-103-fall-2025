input_number = input("Enter a value with 5 digits:")
digit_sum = 0
for digit in input_number:
    digit_sum += int(digit)
if digit_sum % 2 == 0:
    print(f"The sum of digits are even.")
else:
    print(f"The sum of digits are odd.")