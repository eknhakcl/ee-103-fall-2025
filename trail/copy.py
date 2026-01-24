a = [1,2,[45,78,98]]
b = a
print(a)
print(b)
a[2][2]= 56
print(a)
print(b)

import copy

c = copy.deepcopy(a)
print(a)
print(c)
a[2][2]= 46
print(a)
print(c)

