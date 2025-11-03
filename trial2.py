s = input("Enter a string: ")
seen = ""
for char in s:
    if char not in seen:
        seen += char

print(len(seen))