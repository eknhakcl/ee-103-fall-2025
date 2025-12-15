num_str = input("Enter a numbersd separated by commas: ")
numbers_str = num_str.split(",")

numbers_int= [int(x)for x in numbers_str]
print(f"Total number of elements: {len(numbers_int)}")
print(f"Sum of elements: {sum(numbers_int)}")
print(f"Average of elements: {sum(numbers_int)/len(numbers_int)}")
print(f"First element: {numbers_int[0]}")
print(f"Last element: {numbers_int[-1]}")
