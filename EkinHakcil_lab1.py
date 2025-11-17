name = input("Enter a name: ")
number = input("Enter a number: ")

total = 0
for i in number:
    digit = int(i)
    if digit % 2 == 0:
        total += digit

print(f"Sum of even digits: {total}")

last_digit = total % 10
print(f"Last digit of the sum is: {last_digit}")

for x in range(last_digit):
    print(name)
